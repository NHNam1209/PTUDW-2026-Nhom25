import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import {
  Save,
  ArrowLeft,
  Plus,
  Trash2,
  Upload,
  Image as ImageIcon,
  Clock,
  Flame,
  AlertCircle,
  CheckCircle,
} from 'lucide-react';

export const RecipeEditorPage = () => {
  const { id } = useParams();
  const isEditing = Boolean(id);
  const navigate = useNavigate();
  const { user } = useAuth();

  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(isEditing);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [successMsg, setSuccessMsg] = useState(null);

  // Form State
  const [formData, setFormData] = useState({
    title: '',
    categoryId: '',
    difficulty: 'Easy',
    prepTime: 15,
    cookTime: 30,
    servings: 4,
    description: '',
    instructions: '',
    calories: 350,
    protein: 20,
    carbohydrates: 30,
    fat: 10,
    rowVersion: 1,
    status: 0,
  });

  const [ingredients, setIngredients] = useState([
    { name: '', quantity: 1, unit: 'g', notes: '' },
  ]);

  const [steps, setSteps] = useState([
    { stepNumber: 1, title: 'Chuẩn bị nguyên liệu', description: '', timerMinutes: 0 },
  ]);

  const [images, setImages] = useState([]);
  const [uploadingImage, setUploadingImage] = useState(false);

  // Fetch categories & recipe data if editing
  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const catRes = await api.get('/categories');
        setCategories(catRes || []);
        if (!isEditing && catRes?.length > 0) {
          setFormData((prev) => ({ ...prev, categoryId: catRes[0].id }));
        }
      } catch (err) {
        console.error('Failed to fetch categories:', err);
      }
    };

    fetchCategories();

    if (isEditing) {
      const fetchRecipe = async () => {
        try {
          const res = await api.get(`/recipes/${id}`);
          setFormData({
            title: res.title || '',
            categoryId: res.categoryId || '',
            difficulty: res.difficulty || 'Easy',
            prepTime: res.prepTime || 0,
            cookTime: res.cookTime || 0,
            servings: res.servings || 1,
            description: res.description || '',
            instructions: res.instructions || '',
            calories: res.nutrition?.calories || 0,
            protein: res.nutrition?.protein || 0,
            carbohydrates: res.nutrition?.carbohydrates || 0,
            fat: res.nutrition?.fat || 0,
            rowVersion: res.rowVersion || 1,
            status: res.status || 0,
          });

          if (res.ingredients && res.ingredients.length > 0) {
            setIngredients(res.ingredients);
          }
          if (res.steps && res.steps.length > 0) {
            setSteps(res.steps);
          }
          if (res.images && res.images.length > 0) {
            setImages(res.images);
          }
        } catch (err) {
          setError(err.message || 'Không thể tải công thức');
        } finally {
          setLoading(false);
        }
      };
      fetchRecipe();
    }
  }, [id, isEditing]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: ['prepTime', 'cookTime', 'servings', 'calories', 'protein', 'carbohydrates', 'fat'].includes(name)
        ? Number(value)
        : value,
    }));
  };

  // Ingredient helpers
  const handleAddIngredient = () => {
    setIngredients((prev) => [...prev, { name: '', quantity: 1, unit: 'g', notes: '' }]);
  };

  const handleRemoveIngredient = (index) => {
    setIngredients((prev) => prev.filter((_, idx) => idx !== index));
  };

  const handleIngredientChange = (index, field, value) => {
    setIngredients((prev) => {
      const updated = [...prev];
      updated[index] = {
        ...updated[index],
        [field]: field === 'quantity' ? Number(value) : value,
      };
      return updated;
    });
  };

  // Step helpers
  const handleAddStep = () => {
    setSteps((prev) => [
      ...prev,
      { stepNumber: prev.length + 1, title: `Bước ${prev.length + 1}`, description: '', timerMinutes: 0 },
    ]);
  };

  const handleRemoveStep = (index) => {
    setSteps((prev) => {
      const updated = prev.filter((_, idx) => idx !== index);
      return updated.map((step, idx) => ({ ...step, stepNumber: idx + 1 }));
    });
  };

  const handleStepChange = (index, field, value) => {
    setSteps((prev) => {
      const updated = [...prev];
      updated[index] = {
        ...updated[index],
        [field]: field === 'timerMinutes' ? Number(value) : value,
      };
      return updated;
    });
  };

  // Upload image
  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    if (!file || !isEditing) return;

    setUploadingImage(true);
    setError(null);
    try {
      const formPayload = new FormData();
      formPayload.append('file', file);
      formPayload.append('isPrimary', images.length === 0 ? 'true' : 'false');

      const newImg = await api.post(`/recipes/${id}/images`, formPayload);
      setImages((prev) => [...prev, newImg]);
      setSuccessMsg('Đã tải ảnh lên thành công!');
    } catch (err) {
      setError(err.message || 'Lỗi khi tải ảnh lên');
    } finally {
      setUploadingImage(false);
    }
  };

  const handleSubmit = async (targetStatus = 0) => {
    setError(null);
    setSuccessMsg(null);
    setSubmitting(true);

    if (!formData.title.trim()) {
      setError('Vui lòng nhập tên công thức món ăn.');
      setSubmitting(false);
      return;
    }

    if (!formData.categoryId) {
      setError('Vui lòng chọn danh mục cho công thức.');
      setSubmitting(false);
      return;
    }

    const payload = {
      title: formData.title,
      categoryId: formData.categoryId,
      difficulty: formData.difficulty,
      prepTime: formData.prepTime,
      cookTime: formData.cookTime,
      servings: formData.servings,
      description: formData.description,
      instructions: formData.instructions,
      nutrition: {
        calories: formData.calories,
        protein: formData.protein,
        carbohydrates: formData.carbohydrates,
        fat: formData.fat,
      },
      ingredients: ingredients
        .filter((i) => i.name.trim() !== '')
        .map((i, idx) => ({
          name: i.name,
          quantity: i.quantity,
          unit: i.unit,
          notes: i.notes,
          orderIndex: idx + 1,
        })),
      steps: steps
        .filter((s) => s.description.trim() !== '' || s.title.trim() !== '')
        .map((s, idx) => ({
          stepNumber: idx + 1,
          title: s.title || `Bước ${idx + 1}`,
          description: s.description,
          timerMinutes: s.timerMinutes || 0,
        })),
    };

    try {
      if (isEditing) {
        await api.put(`/recipes/${id}`, {
          ...payload,
          rowVersion: formData.rowVersion,
        });

        if (targetStatus === 1 && formData.status === 0) {
          await api.patch(`/recipes/${id}/publish`);
        }

        setSuccessMsg('Cập nhật công thức thành công!');
        setTimeout(() => navigate('/dashboard'), 1000);
      } else {
        const created = await api.post('/recipes', payload);
        if (targetStatus === 1 && created?.id) {
          await api.patch(`/recipes/${created.id}/publish`);
        }
        setSuccessMsg('Tạo công thức mới thành công!');
        setTimeout(() => navigate('/dashboard'), 1000);
      }
    } catch (err) {
      setError(err.message || 'Không thể lưu công thức');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="container" style={{ padding: '5rem 1rem', textAlign: 'center', color: 'var(--text-muted)' }}>
        Đang tải thông tin công thức...
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 6rem', maxWidth: '960px' }}>
      
      {/* Header bar */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <Link to="/dashboard" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.375rem', color: 'var(--text-muted)', fontSize: '0.875rem', marginBottom: '0.5rem' }}>
            <ArrowLeft size={16} /> Quay lại Dashboard
          </Link>
          <h1 style={{ fontSize: '1.875rem' }}>
            {isEditing ? 'Chỉnh Sửa Công Thức' : 'Tạo Mới Công Thức Ẩm Thực'}
          </h1>
        </div>

        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button
            type="button"
            className="btn btn-outline"
            disabled={submitting}
            onClick={() => handleSubmit(0)}
          >
            <Save size={16} />
            <span>Lưu Nháp</span>
          </button>
          <button
            type="button"
            className="btn btn-primary"
            disabled={submitting}
            onClick={() => handleSubmit(1)}
          >
            <CheckCircle size={16} />
            <span>Xuất Bản Ngay</span>
          </button>
        </div>
      </div>

      {error && (
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
          <AlertCircle size={18} />
          <span>{error}</span>
        </div>
      )}

      {successMsg && (
        <div className="alert alert-success" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
          <CheckCircle size={18} />
          <span>{successMsg}</span>
        </div>
      )}

      <form onSubmit={(e) => { e.preventDefault(); handleSubmit(0); }} style={{ display: 'flex', flexDirection: 'column', gap: '2rem' }}>
        
        {/* Section 1: Thông tin cơ bản */}
        <div className="card" style={{ padding: '2rem' }}>
          <h2 style={{ fontSize: '1.25rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--border)', paddingBottom: '0.75rem' }}>
            1. Thông Tin Chung
          </h2>

          <div className="form-group" style={{ marginBottom: '1.25rem' }}>
            <label className="form-label" style={{ fontWeight: 600 }}>Tên món ăn / Tiêu đề công thức *</label>
            <input
              type="text"
              name="title"
              className="form-control"
              placeholder="VD: Phở Bò Tái Lăn Hà Nội Chuẩn Vị"
              value={formData.title}
              onChange={handleInputChange}
              required
            />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.25rem', marginBottom: '1.25rem' }}>
            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Danh mục ẩm thực *</label>
              <select
                name="categoryId"
                className="form-control"
                value={formData.categoryId}
                onChange={handleInputChange}
                required
              >
                <option value="">-- Chọn danh mục --</option>
                {categories.map((c) => (
                  <option key={c.id} value={c.id}>{c.name}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Độ khó</label>
              <select
                name="difficulty"
                className="form-control"
                value={formData.difficulty}
                onChange={handleInputChange}
              >
                <option value="Easy">Dễ (Easy)</option>
                <option value="Medium">Trung bình (Medium)</option>
                <option value="Hard">Khó (Hard)</option>
              </select>
            </div>

            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Khẩu phần (Người)</label>
              <input
                type="number"
                name="servings"
                min="1"
                className="form-control"
                value={formData.servings}
                onChange={handleInputChange}
              />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.25rem', marginBottom: '1.25rem' }}>
            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Thời gian chuẩn bị (Phút)</label>
              <input
                type="number"
                name="prepTime"
                min="0"
                className="form-control"
                value={formData.prepTime}
                onChange={handleInputChange}
              />
            </div>

            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Thời gian nấu (Phút)</label>
              <input
                type="number"
                name="cookTime"
                min="0"
                className="form-control"
                value={formData.cookTime}
                onChange={handleInputChange}
              />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label" style={{ fontWeight: 600 }}>Mô tả ngắn gọn về món ăn</label>
            <textarea
              name="description"
              rows={3}
              className="form-control"
              placeholder="Chia sẻ đôi nét về nguồn gốc, hương vị hoặc kỷ niệm gắn liền với món ăn này..."
              value={formData.description}
              onChange={handleInputChange}
            />
          </div>
        </div>

        {/* Section 2: Dinh dưỡng */}
        <div className="card" style={{ padding: '2rem' }}>
          <h2 style={{ fontSize: '1.25rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--border)', paddingBottom: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Flame size={18} color="var(--primary)" /> 2. Giá Trị Dinh Dưỡng (Mỗi Khẩu Phần)
          </h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(140px, 1fr))', gap: '1rem' }}>
            <div className="form-group">
              <label className="form-label">Calories (kcal)</label>
              <input
                type="number"
                name="calories"
                className="form-control"
                value={formData.calories}
                onChange={handleInputChange}
              />
            </div>
            <div className="form-group">
              <label className="form-label">Protein (g)</label>
              <input
                type="number"
                name="protein"
                className="form-control"
                value={formData.protein}
                onChange={handleInputChange}
              />
            </div>
            <div className="form-group">
              <label className="form-label">Carbs (g)</label>
              <input
                type="number"
                name="carbohydrates"
                className="form-control"
                value={formData.carbohydrates}
                onChange={handleInputChange}
              />
            </div>
            <div className="form-group">
              <label className="form-label">Chất béo / Fat (g)</label>
              <input
                type="number"
                name="fat"
                className="form-control"
                value={formData.fat}
                onChange={handleInputChange}
              />
            </div>
          </div>
        </div>

        {/* Section 3: Nguyên liệu */}
        <div className="card" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '1px solid var(--border)', paddingBottom: '0.75rem' }}>
            <h2 style={{ fontSize: '1.25rem' }}>3. Danh Sách Nguyên Liệu</h2>
            <button
              type="button"
              onClick={handleAddIngredient}
              className="btn btn-outline btn-sm"
            >
              <Plus size={14} /> Thêm nguyên liệu
            </button>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {ingredients.map((ing, idx) => (
              <div key={idx} style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 1fr 2fr auto', gap: '0.75rem', alignItems: 'center' }}>
                <input
                  type="text"
                  placeholder="Tên nguyên liệu (VD: Thịt thăn bò)"
                  className="form-control"
                  value={ing.name}
                  onChange={(e) => handleIngredientChange(idx, 'name', e.target.value)}
                />
                <input
                  type="number"
                  step="0.1"
                  placeholder="Số lượng"
                  className="form-control"
                  value={ing.quantity}
                  onChange={(e) => handleIngredientChange(idx, 'quantity', e.target.value)}
                />
                <input
                  type="text"
                  placeholder="Đơn vị (g, muỗng...)"
                  className="form-control"
                  value={ing.unit}
                  onChange={(e) => handleIngredientChange(idx, 'unit', e.target.value)}
                />
                <input
                  type="text"
                  placeholder="Ghi chú (tùy chọn)"
                  className="form-control"
                  value={ing.notes || ''}
                  onChange={(e) => handleIngredientChange(idx, 'notes', e.target.value)}
                />
                <button
                  type="button"
                  onClick={() => handleRemoveIngredient(idx)}
                  className="btn btn-sm"
                  style={{ backgroundColor: '#fef2f2', color: '#dc2626', padding: '0.5rem' }}
                  title="Xóa dòng"
                >
                  <Trash2 size={16} />
                </button>
              </div>
            ))}
          </div>
        </div>

        {/* Section 4: Các bước thực hiện */}
        <div className="card" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', borderBottom: '1px solid var(--border)', paddingBottom: '0.75rem' }}>
            <h2 style={{ fontSize: '1.25rem' }}>4. Các Bước Nấu Ăn (Có Hẹn Giờ Timer)</h2>
            <button
              type="button"
              onClick={handleAddStep}
              className="btn btn-outline btn-sm"
            >
              <Plus size={14} /> Thêm bước thực hiện
            </button>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {steps.map((st, idx) => (
              <div key={idx} style={{ padding: '1.25rem', border: '1px solid var(--border)', borderRadius: '0.75rem', backgroundColor: '#fcfcfc' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                  <span style={{ fontWeight: 700, fontSize: '0.9375rem', color: 'var(--primary)' }}>
                    Bước {idx + 1}
                  </span>
                  {steps.length > 1 && (
                    <button
                      type="button"
                      onClick={() => handleRemoveStep(idx)}
                      className="btn btn-sm"
                      style={{ backgroundColor: '#fef2f2', color: '#dc2626' }}
                    >
                      <Trash2 size={14} /> Xóa bước này
                    </button>
                  )}
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
                  <div className="form-group">
                    <label className="form-label">Tiêu đề bước</label>
                    <input
                      type="text"
                      className="form-control"
                      placeholder="VD: Xào sơ thịt bò với lửa lớn"
                      value={st.title}
                      onChange={(e) => handleStepChange(idx, 'title', e.target.value)}
                    />
                  </div>
                  <div className="form-group">
                    <label className="form-label" style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                      <Clock size={14} /> Hẹn giờ (Phút)
                    </label>
                    <input
                      type="number"
                      min="0"
                      className="form-control"
                      placeholder="0 nếu không cần"
                      value={st.timerMinutes}
                      onChange={(e) => handleStepChange(idx, 'timerMinutes', e.target.value)}
                    />
                  </div>
                </div>

                <div className="form-group">
                  <label className="form-label">Mô tả chi tiết cách làm</label>
                  <textarea
                    rows={3}
                    className="form-control"
                    placeholder="Mô tả kỹ thuật nấu, nhiệt độ, dấu hiệu món ăn đạt yêu cầu..."
                    value={st.description}
                    onChange={(e) => handleStepChange(idx, 'description', e.target.value)}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Section 5: Quản lý hình ảnh (chỉ khi đang edit) */}
        {isEditing && (
          <div className="card" style={{ padding: '2rem' }}>
            <h2 style={{ fontSize: '1.25rem', marginBottom: '1.5rem', borderBottom: '1px solid var(--border)', paddingBottom: '0.75rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <ImageIcon size={18} /> 5. Hình Ảnh Món Ăn
            </h2>

            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem', marginBottom: '1.5rem' }}>
              {images.map((img) => (
                <div key={img.id} style={{ position: 'relative', width: '120px', height: '120px', borderRadius: '0.5rem', overflow: 'hidden', border: img.isPrimary ? '3px solid var(--primary)' : '1px solid var(--border)' }}>
                  <img
                    src={img.thumbnailUrl || img.originalUrl}
                    alt="recipe"
                    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                  />
                  {img.isPrimary && (
                    <span style={{ position: 'absolute', bottom: 4, left: 4, background: 'var(--primary)', color: '#fff', fontSize: '0.625rem', padding: '2px 6px', borderRadius: '4px', fontWeight: 700 }}>
                      Ảnh chính
                    </span>
                  )}
                </div>
              ))}
            </div>

            <div style={{ border: '2px dashed var(--border)', borderRadius: '0.75rem', padding: '2rem', textAlign: 'center', backgroundColor: '#fafafa' }}>
              <Upload size={32} style={{ margin: '0 auto 0.75rem', color: 'var(--text-muted)' }} />
              <p style={{ fontWeight: 600, marginBottom: '0.25rem' }}>Tải lên hình ảnh món ăn mới</p>
              <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', marginBottom: '1rem' }}>
                Hỗ trợ định dạng JPG, PNG, WEBP (Tối đa 10MB)
              </p>
              <label className="btn btn-outline btn-sm" style={{ cursor: 'pointer' }}>
                <span>{uploadingImage ? 'Đang tải lên...' : 'Chọn tập tin ảnh'}</span>
                <input
                  type="file"
                  accept="image/*"
                  style={{ display: 'none' }}
                  onChange={handleImageUpload}
                  disabled={uploadingImage}
                />
              </label>
            </div>
          </div>
        )}

        {/* Bottom Actions */}
        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '1rem', paddingTop: '1rem' }}>
          <Link to="/dashboard" className="btn btn-outline">
            Hủy bỏ
          </Link>
          <button
            type="button"
            className="btn btn-outline"
            disabled={submitting}
            onClick={() => handleSubmit(0)}
          >
            <Save size={16} />
            <span>Lưu Bản Nháp</span>
          </button>
          <button
            type="button"
            className="btn btn-primary"
            disabled={submitting}
            onClick={() => handleSubmit(1)}
          >
            <CheckCircle size={16} />
            <span>{isEditing ? 'Cập Nhật & Xuất Bản' : 'Tạo & Xuất Bản Ngay'}</span>
          </button>
        </div>

      </form>
    </div>
  );
};
