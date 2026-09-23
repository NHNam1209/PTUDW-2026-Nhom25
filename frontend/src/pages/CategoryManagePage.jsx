import React, { useState, useEffect } from 'react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import { Plus, Edit2, Trash2, Tag, AlertCircle, CheckCircle, RefreshCw } from 'lucide-react';

export const CategoryManagePage = () => {
  const { user } = useAuth();
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Form state
  const [editingCategory, setEditingCategory] = useState(null);
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [submitting, setSubmitting] = useState(false);

  const fetchCategories = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await api.get('/categories');
      setCategories(res || []);
    } catch (err) {
      setError(err.message || 'Không thể tải danh sách danh mục');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCategories();
  }, []);

  const handleStartEdit = (cat) => {
    setEditingCategory(cat);
    setName(cat.name);
    setDescription(cat.description || '');
    setError(null);
    setSuccess(null);
  };

  const handleCancel = () => {
    setEditingCategory(null);
    setName('');
    setDescription('');
    setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name.trim()) {
      setError('Vui lòng nhập tên danh mục.');
      return;
    }

    setSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      if (editingCategory) {
        await api.put(`/categories/${editingCategory.id}`, {
          name: name.trim(),
          description: description.trim(),
        });
        setSuccess(`Đã cập nhật danh mục "${name}"!`);
      } else {
        await api.post('/categories', {
          name: name.trim(),
          description: description.trim(),
        });
        setSuccess(`Đã thêm danh mục mới "${name}"!`);
      }

      handleCancel();
      fetchCategories();
    } catch (err) {
      setError(err.message || 'Thao tác thất bại');
    } finally {
      setSubmitting(false);
    }
  };

  const handleDelete = async (cat) => {
    if (window.confirm(`Bạn có chắc chắn muốn xóa danh mục "${cat.name}" không?`)) {
      setError(null);
      setSuccess(null);
      try {
        await api.delete(`/categories/${cat.id}`);
        setSuccess(`Đã xóa danh mục "${cat.name}"!`);
        fetchCategories();
      } catch (err) {
        setError(err.message || 'Không thể xóa danh mục (có thể đang có công thức thuộc danh mục này)');
      }
    }
  };

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 6rem', maxWidth: '1000px' }}>
      
      {/* Title */}
      <div style={{ marginBottom: '2.5rem' }}>
        <h1 style={{ fontSize: '1.875rem', marginBottom: '0.25rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Tag color="var(--primary)" /> Quản Lý Danh Mục Ẩm Thực
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
          Tạo và điều chỉnh các danh mục để phân loại công thức nấu ăn trên toàn hệ thống.
        </p>
      </div>

      {error && (
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
          <AlertCircle size={18} />
          <span>{error}</span>
        </div>
      )}

      {success && (
        <div className="alert alert-success" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.5rem' }}>
          <CheckCircle size={18} />
          <span>{success}</span>
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.6fr', gap: '2rem', alignItems: 'flex-start' }}>
        
        {/* Form Card */}
        <div className="card" style={{ padding: '1.75rem' }}>
          <h2 style={{ fontSize: '1.125rem', marginBottom: '1.25rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            {editingCategory ? <Edit2 size={16} /> : <Plus size={16} />}
            <span>{editingCategory ? 'Chỉnh Sửa Danh Mục' : 'Thêm Danh Mục Mới'}</span>
          </h2>

          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Tên danh mục *</label>
              <input
                type="text"
                className="form-control"
                placeholder="VD: Món Chay Thanh Đạm"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label" style={{ fontWeight: 600 }}>Mô tả danh mục</label>
              <textarea
                rows={3}
                className="form-control"
                placeholder="Mô tả đặc điểm hoặc các món ăn trong danh mục này..."
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              />
            </div>

            <div style={{ display: 'flex', gap: '0.75rem', marginTop: '0.5rem' }}>
              <button
                type="submit"
                className="btn btn-primary"
                disabled={submitting}
                style={{ flex: 1 }}
              >
                {submitting ? 'Đang lưu...' : editingCategory ? 'Cập Nhật' : 'Tạo Danh Mục'}
              </button>
              {editingCategory && (
                <button
                  type="button"
                  onClick={handleCancel}
                  className="btn btn-outline"
                >
                  Hủy
                </button>
              )}
            </div>
          </form>
        </div>

        {/* Category List Card */}
        <div className="card" style={{ overflow: 'hidden' }}>
          <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h2 style={{ fontSize: '1.125rem' }}>Các Danh Mục Hiện Có</h2>
            <button
              onClick={fetchCategories}
              className="btn btn-outline btn-sm"
              title="Làm mới"
            >
              <RefreshCw size={14} />
            </button>
          </div>

          {loading ? (
            <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
              Đang tải danh mục...
            </div>
          ) : categories.length > 0 ? (
            <div style={{ overflowX: 'auto' }}>
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.875rem' }}>
                <thead>
                  <tr style={{ backgroundColor: '#f8fafc', borderBottom: '1px solid var(--border)', color: 'var(--text-muted)', fontSize: '0.75rem', textTransform: 'uppercase' }}>
                    <th style={{ padding: '0.75rem 1rem' }}>Tên danh mục</th>
                    <th style={{ padding: '0.75rem 1rem' }}>Slug</th>
                    <th style={{ padding: '0.75rem 1rem', textAlign: 'right' }}>Thao tác</th>
                  </tr>
                </thead>
                <tbody>
                  {categories.map((c) => (
                    <tr key={c.id} style={{ borderBottom: '1px solid var(--border)' }}>
                      <td style={{ padding: '0.875rem 1rem' }}>
                        <div style={{ fontWeight: 600, color: 'var(--secondary)' }}>{c.name}</div>
                        {c.description && (
                          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '2px' }}>
                            {c.description}
                          </div>
                        )}
                      </td>
                      <td style={{ padding: '0.875rem 1rem', color: 'var(--text-muted)', fontSize: '0.8125rem' }}>
                        {c.slug}
                      </td>
                      <td style={{ padding: '0.875rem 1rem', textAlign: 'right' }}>
                        <div style={{ display: 'inline-flex', gap: '0.375rem' }}>
                          <button
                            onClick={() => handleStartEdit(c)}
                            className="btn btn-outline btn-sm"
                            title="Sửa danh mục"
                          >
                            <Edit2 size={13} />
                          </button>
                          <button
                            onClick={() => handleDelete(c)}
                            className="btn btn-sm"
                            style={{ backgroundColor: '#fef2f2', color: '#dc2626' }}
                            title="Xóa danh mục"
                          >
                            <Trash2 size={13} />
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          ) : (
            <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
              Chưa có danh mục nào. Hãy thêm danh mục đầu tiên!
            </div>
          )}
        </div>

      </div>
    </div>
  );
};
