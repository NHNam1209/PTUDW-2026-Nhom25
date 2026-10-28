import { useEffect, useMemo, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import {
  AlertCircle,
  ArrowLeft,
  Carrot,
  Check,
  CheckCircle,
  ChevronLeft,
  ChevronRight,
  Flame,
  Image as ImageIcon,
  Info,
  ListOrdered,
  Save,
  Send,
} from 'lucide-react';
import { api } from '../api/client';
import { ImageUploader } from '../components/editor/ImageUploader';
import { IngredientEditor } from '../components/editor/IngredientEditor';
import { StepEditor } from '../components/editor/StepEditor';
import {
  DIFFICULTY_OPTIONS,
  STATUS_LABELS,
  buildRecipePayload,
  createEmptyForm,
  createEmptyIngredient,
  createEmptyStep,
  formFromRecipe,
  ingredientsFromRecipe,
  stepsFromRecipe,
  validateInfoStep,
  validateIngredients,
  validateNutrition,
  validateSteps,
} from '../utils/recipeForm';
import {
  setPrimaryImage,
  syncIngredients,
  syncSteps,
  uploadQueuedImages,
} from '../utils/recipeApi';
import '../styles/editor.css';

const WIZARD_STEPS = [
  { key: 'info', label: 'Thông tin', icon: Info },
  { key: 'nutrition', label: 'Dinh dưỡng', icon: Flame },
  { key: 'ingredients', label: 'Nguyên liệu', icon: Carrot },
  { key: 'steps', label: 'Các bước', icon: ListOrdered },
  { key: 'images', label: 'Hình ảnh', icon: ImageIcon },
];

export const RecipeEditorPage = () => {
  const { id } = useParams();
  const isEditing = Boolean(id);
  const navigate = useNavigate();

  const [categories, setCategories] = useState([]);
  const [form, setForm] = useState(createEmptyForm);
  const [ingredients, setIngredients] = useState([]);
  const [steps, setSteps] = useState([]);
  const [originalIngredients, setOriginalIngredients] = useState([]);
  const [originalSteps, setOriginalSteps] = useState([]);
  const [recipeMeta, setRecipeMeta] = useState(null);
  const [imageState, setImageState] = useState({ uploaded: [], pending: [], coverKey: null });
  const [pendingProgress, setPendingProgress] = useState({});

  const [stepIndex, setStepIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [savingPhase, setSavingPhase] = useState('');
  const [error, setError] = useState(null);
  const [touched, setTouched] = useState(false);

  useEffect(() => {
    let active = true;

    const load = async () => {
      setLoading(true);
      setError(null);

      try {
        const categoryList = await api.get('/categories');
        if (!active) return;
        setCategories(categoryList || []);

        if (isEditing) {
          const recipe = await api.get(`/recipes/${id}`);
          if (!active) return;

          setForm(formFromRecipe(recipe));

          const loadedIngredients = ingredientsFromRecipe(recipe);
          const loadedSteps = stepsFromRecipe(recipe);
          setIngredients(loadedIngredients);
          setOriginalIngredients(loadedIngredients);
          setSteps(loadedSteps);
          setOriginalSteps(loadedSteps);

          const loadedImages = recipe.images || [];
          const primaryImage = loadedImages.find((image) => image.isPrimary);
          setImageState({
            uploaded: loadedImages,
            pending: [],
            coverKey: primaryImage?.id || loadedImages[0]?.id || null,
          });

          setRecipeMeta({
            status: recipe.status,
            slug: recipe.slug,
            rowVersion: recipe.rowVersion ?? 1,
          });
        } else {
          const defaultIngredient = createEmptyIngredient();
          const defaultStep = createEmptyStep(0);
          setIngredients([defaultIngredient]);
          setSteps([defaultStep]);
          setForm((prev) => ({
            ...prev,
            categoryId: categoryList?.[0]?.id || '',
          }));
        }
      } catch (err) {
        if (active) {
          setError(err.message || 'Không thể tải dữ liệu công thức.');
        }
      } finally {
        if (active) setLoading(false);
      }
    };

    load();

    return () => {
      active = false;
    };
  }, [id, isEditing]);

  const infoErrors = useMemo(() => validateInfoStep(form), [form]);
  const nutritionErrors = useMemo(() => validateNutrition(form), [form]);
  const ingredientError = useMemo(() => validateIngredients(ingredients), [ingredients]);
  const stepError = useMemo(() => validateSteps(steps), [steps]);

  const stepCompletion = [
    Object.keys(infoErrors).length === 0,
    Object.keys(nutritionErrors).length === 0,
    ingredientError === null,
    stepError === null,
    imageState.uploaded.length + imageState.pending.length > 0,
  ];

  const handleFieldChange = (event) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const currentStep = WIZARD_STEPS[stepIndex];

  const goToStep = (index) => {
    setTouched(false);
    setStepIndex(index);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const validateCurrentStep = () => {
    if (currentStep.key === 'info' && Object.keys(infoErrors).length > 0) {
      setTouched(true);
      return false;
    }
    if (currentStep.key === 'nutrition' && Object.keys(nutritionErrors).length > 0) {
      setTouched(true);
      return false;
    }
    if (currentStep.key === 'ingredients' && ingredientError) {
      setTouched(true);
      return false;
    }
    if (currentStep.key === 'steps' && stepError) {
      setTouched(true);
      return false;
    }
    return true;
  };

  const handleNext = () => {
    if (!validateCurrentStep()) return;
    goToStep(Math.min(stepIndex + 1, WIZARD_STEPS.length - 1));
  };

  const handleBack = () => {
    goToStep(Math.max(stepIndex - 1, 0));
  };

  const handleSave = async (publishAfterSave) => {
    setTouched(true);
    setError(null);

    if (Object.keys(infoErrors).length > 0) {
      setStepIndex(0);
      setError('Vui lòng hoàn thiện thông tin chung trước khi lưu.');
      return;
    }
    if (Object.keys(nutritionErrors).length > 0) {
      setStepIndex(1);
      setError('Giá trị dinh dưỡng chưa hợp lệ.');
      return;
    }
    if (ingredientError) {
      setStepIndex(2);
      setError(ingredientError);
      return;
    }
    if (stepError) {
      setStepIndex(3);
      setError(stepError);
      return;
    }

    setSaving(true);
    setSavingPhase('Đang lưu thông tin...');
    setPendingProgress({});

    const progressHandler = (uid, percent) => {
      setPendingProgress((prev) => ({ ...prev, [uid]: percent }));
    };

    try {
      const payload = buildRecipePayload(form);

      if (isEditing) {
        await api.put(`/recipes/${id}`, {
          ...payload,
          rowVersion: recipeMeta?.rowVersion,
        });
        await syncIngredients(id, originalIngredients, ingredients);
        await syncSteps(id, originalSteps, steps);

        if (imageState.coverKey && !String(imageState.coverKey).startsWith('pending:')) {
          const coverImage = imageState.uploaded.find((image) => image.id === imageState.coverKey);
          if (coverImage && !coverImage.isPrimary) {
            await setPrimaryImage(id, coverImage.id);
          }
        }

        if (imageState.pending.length > 0) {
          setSavingPhase('Đang tải ảnh lên...');
          await uploadQueuedImages(id, imageState.pending, imageState.coverKey, progressHandler);
        }

        if (publishAfterSave) {
          setSavingPhase('Đang xuất bản công thức...');
          await api.patch(`/recipes/${id}/publish`);
        }
      } else {
        const created = await api.post('/recipes', {
          ...payload,
          ingredients: ingredients.map((ingredient, index) => ({
            name: ingredient.name.trim(),
            quantity: ingredient.quantity === '' ? null : Number(ingredient.quantity),
            unit: ingredient.unit.trim() || null,
            notes: ingredient.notes.trim() || null,
            orderIndex: index,
          })),
          steps: steps.map((step) => ({
            title: step.title.trim(),
            description: step.description.trim(),
            timerMinutes: step.timerMinutes === '' ? 0 : Number(step.timerMinutes),
          })),
        });

        if (imageState.pending.length > 0) {
          setSavingPhase('Đang tải ảnh lên...');
          await uploadQueuedImages(created.id, imageState.pending, imageState.coverKey, progressHandler);
        }

        if (publishAfterSave) {
          setSavingPhase('Đang xuất bản công thức...');
          await api.patch(`/recipes/${created.id}/publish`);
        }
      }

      navigate('/dashboard/recipes');
    } catch (err) {
      setError(err.message || 'Không thể lưu công thức.');
      setSavingPhase('');
    } finally {
      setSaving(false);
      setPendingProgress({});
    }
  };

  if (loading) {
    return (
      <div className="editor-shell" style={{ textAlign: 'center', color: 'var(--text-muted)', paddingTop: '6rem' }}>
        Đang tải dữ liệu công thức...
      </div>
    );
  }

  return (
    <div className="editor-shell">
      <div className="editor-header">
        <div>
          <Link
            to="/dashboard/recipes"
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.375rem',
              fontSize: '0.8125rem',
              color: 'var(--text-muted)',
              marginBottom: '0.5rem',
            }}
          >
            <ArrowLeft size={14} />
            <span>Quay lại danh sách công thức</span>
          </Link>
          <h1 style={{ fontSize: '1.875rem', marginBottom: '0.25rem' }}>
            {isEditing ? 'Chỉnh Sửa Công Thức' : 'Tạo Công Thức Mới'}
          </h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
            Hoàn thành {WIZARD_STEPS.length} bước để có một công thức hoàn chỉnh.
          </p>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', flexWrap: 'wrap' }}>
          {isEditing && recipeMeta && (
            <span
              className={`badge ${recipeMeta.status === 1 ? 'badge-published' : recipeMeta.status === 2 ? 'badge-archived' : 'badge-draft'}`}
              style={{ alignSelf: 'center' }}
            >
              {STATUS_LABELS[recipeMeta.status] || 'Bản nháp'}
            </span>
          )}
          <button type="button" className="btn btn-outline" onClick={() => handleSave(false)} disabled={saving}>
            <Save size={16} />
            <span>{saving ? 'Đang lưu...' : 'Lưu nháp'}</span>
          </button>
          <button type="button" className="btn btn-primary" onClick={() => handleSave(true)} disabled={saving}>
            <Send size={16} />
            <span>Xuất bản</span>
          </button>
        </div>
      </div>

      {error && (
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <AlertCircle size={18} />
          <span>{error}</span>
        </div>
      )}

      {saving && savingPhase && (
        <div
          className="alert"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            backgroundColor: 'var(--primary-light)',
            border: '1px solid #fed7aa',
            color: '#9a3412',
          }}
        >
          <span>{savingPhase}</span>
        </div>
      )}

      <nav className="editor-rail" aria-label="Các bước tạo công thức">
        {WIZARD_STEPS.map((wizardStep, index) => {
          const Icon = wizardStep.icon;
          const isActive = index === stepIndex;
          const isDone = stepCompletion[index] && index !== stepIndex;

          return (
            <button
              key={wizardStep.key}
              type="button"
              className={`editor-rail-item${isActive ? ' active' : ''}${isDone ? ' done' : ''}`}
              onClick={() => goToStep(index)}
              aria-current={isActive ? 'step' : undefined}
            >
              <span className="editor-rail-index">
                {isDone ? <Check size={13} /> : <Icon size={13} />}
              </span>
              <span>{wizardStep.label}</span>
            </button>
          );
        })}
      </nav>

      <section className="editor-card">
        {currentStep.key === 'info' && (
          <>
            <h2 className="editor-section-title">1. Thông Tin Chung</h2>

            <div className="field">
              <label className="field-label" htmlFor="title">
                Tên món ăn / Tiêu đề công thức *
              </label>
              <input
                id="title"
                name="title"
                type="text"
                className={`input${touched && infoErrors.title ? ' input-error' : ''}`}
                placeholder="VD: Phở Bò Tái Lăn Hà Nội Chuẩn Vị"
                value={form.title}
                onChange={handleFieldChange}
              />
              {touched && infoErrors.title && <span className="field-error">{infoErrors.title}</span>}
              <span className="field-hint">Từ 5 đến 200 ký tự.</span>
            </div>

            <div className="editor-grid">
              <div className="field">
                <label className="field-label" htmlFor="categoryId">Danh mục ẩm thực *</label>
                <select
                  id="categoryId"
                  name="categoryId"
                  className={`select${touched && infoErrors.categoryId ? ' input-error' : ''}`}
                  value={form.categoryId}
                  onChange={handleFieldChange}
                >
                  <option value="">-- Chọn danh mục --</option>
                  {categories.map((category) => (
                    <option key={category.id} value={category.id}>{category.name}</option>
                  ))}
                </select>
                {touched && infoErrors.categoryId && <span className="field-error">{infoErrors.categoryId}</span>}
              </div>

              <div className="field">
                <label className="field-label" htmlFor="difficulty">Độ khó</label>
                <select
                  id="difficulty"
                  name="difficulty"
                  className="select"
                  value={form.difficulty}
                  onChange={handleFieldChange}
                >
                  {DIFFICULTY_OPTIONS.map((option) => (
                    <option key={option.value} value={option.value}>{option.label}</option>
                  ))}
                </select>
              </div>

              <div className="field">
                <label className="field-label" htmlFor="servings">Khẩu phần (người) *</label>
                <input
                  id="servings"
                  name="servings"
                  type="number"
                  min="1"
                  className={`input${touched && infoErrors.servings ? ' input-error' : ''}`}
                  value={form.servings}
                  onChange={handleFieldChange}
                />
                {touched && infoErrors.servings && <span className="field-error">{infoErrors.servings}</span>}
              </div>

              <div className="field">
                <label className="field-label" htmlFor="prepTimeMinutes">Chuẩn bị (phút) *</label>
                <input
                  id="prepTimeMinutes"
                  name="prepTimeMinutes"
                  type="number"
                  min="1"
                  className={`input${touched && infoErrors.prepTimeMinutes ? ' input-error' : ''}`}
                  value={form.prepTimeMinutes}
                  onChange={handleFieldChange}
                />
                {touched && infoErrors.prepTimeMinutes && <span className="field-error">{infoErrors.prepTimeMinutes}</span>}
              </div>

              <div className="field">
                <label className="field-label" htmlFor="cookTimeMinutes">Nấu (phút) *</label>
                <input
                  id="cookTimeMinutes"
                  name="cookTimeMinutes"
                  type="number"
                  min="0"
                  className={`input${touched && infoErrors.cookTimeMinutes ? ' input-error' : ''}`}
                  value={form.cookTimeMinutes}
                  onChange={handleFieldChange}
                />
                {touched && infoErrors.cookTimeMinutes && <span className="field-error">{infoErrors.cookTimeMinutes}</span>}
              </div>
            </div>

            <div className="field" style={{ marginTop: '1.25rem' }}>
              <label className="field-label" htmlFor="description">Mô tả ngắn về món ăn *</label>
              <textarea
                id="description"
                name="description"
                rows={3}
                className={`textarea${touched && infoErrors.description ? ' input-error' : ''}`}
                placeholder="Nguồn gốc, hương vị hoặc câu chuyện gắn liền với món ăn..."
                value={form.description}
                onChange={handleFieldChange}
              />
              {touched && infoErrors.description && <span className="field-error">{infoErrors.description}</span>}
              <span className="field-hint">{form.description.trim().length} ký tự (tối thiểu 10).</span>
            </div>

            <div className="field">
              <label className="field-label" htmlFor="instructions">Hướng dẫn tổng quan (tùy chọn)</label>
              <textarea
                id="instructions"
                name="instructions"
                rows={3}
                className="textarea"
                placeholder="Ghi chú chung, mẹo nấu ăn hoặc lưu ý trước khi bắt đầu..."
                value={form.instructions}
                onChange={handleFieldChange}
              />
            </div>
          </>
        )}

        {currentStep.key === 'nutrition' && (
          <>
            <h2 className="editor-section-title">2. Dinh Dưỡng (mỗi khẩu phần)</h2>
            <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
              Các trường không bắt buộc. Bạn có thể để trống nếu chưa ước tính được.
            </p>

            <div className="editor-grid">
              {[
                { name: 'calories', label: 'Calories (kcal)' },
                { name: 'protein', label: 'Protein (g)' },
                { name: 'carbohydrates', label: 'Carbohydrate (g)' },
                { name: 'fat', label: 'Chất béo (g)' },
                { name: 'fiber', label: 'Chất xơ (g)' },
                { name: 'sodium', label: 'Natri (mg)' },
              ].map((field) => (
                <div className="field" key={field.name}>
                  <label className="field-label" htmlFor={field.name}>{field.label}</label>
                  <input
                    id={field.name}
                    name={field.name}
                    type="number"
                    min="0"
                    step="0.1"
                    className={`input${touched && nutritionErrors[field.name] ? ' input-error' : ''}`}
                    value={form[field.name]}
                    onChange={handleFieldChange}
                  />
                  {touched && nutritionErrors[field.name] && (
                    <span className="field-error">{nutritionErrors[field.name]}</span>
                  )}
                </div>
              ))}
            </div>
          </>
        )}

        {currentStep.key === 'ingredients' && (
          <IngredientEditor
            ingredients={ingredients}
            onChange={setIngredients}
            error={touched ? ingredientError : null}
          />
        )}

        {currentStep.key === 'steps' && (
          <StepEditor
            steps={steps}
            onChange={setSteps}
            error={touched ? stepError : null}
          />
        )}

        {currentStep.key === 'images' && (
          <ImageUploader
            recipeId={isEditing ? id : null}
            value={imageState}
            onChange={setImageState}
            pendingProgress={pendingProgress}
          />
        )}

        <div className="editor-actions">
          <button type="button" className="btn btn-outline" onClick={handleBack} disabled={stepIndex === 0}>
            <ChevronLeft size={16} />
            <span>Trước</span>
          </button>

          <div className="editor-actions-right">
            <span style={{ alignSelf: 'center', fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
              Bước {stepIndex + 1}/{WIZARD_STEPS.length}
            </span>

            {stepIndex < WIZARD_STEPS.length - 1 ? (
              <button type="button" className="btn btn-primary" onClick={handleNext}>
                <span>Tiếp tục</span>
                <ChevronRight size={16} />
              </button>
            ) : (
              <>
                <button type="button" className="btn btn-outline" onClick={() => handleSave(false)} disabled={saving}>
                  <Save size={16} />
                  <span>{saving ? 'Đang lưu...' : 'Lưu nháp'}</span>
                </button>
                <button type="button" className="btn btn-primary" onClick={() => handleSave(true)} disabled={saving}>
                  <CheckCircle size={16} />
                  <span>{isEditing ? 'Cập nhật & Xuất bản' : 'Tạo & Xuất bản'}</span>
                </button>
              </>
            )}
          </div>
        </div>
      </section>
    </div>
  );
};
