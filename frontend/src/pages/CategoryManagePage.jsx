import { useCallback, useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import {
  AlertCircle,
  ArrowLeft,
  CheckCircle,
  Edit2,
  FolderTree,
  Plus,
  RefreshCw,
  Tag,
  Trash2,
} from 'lucide-react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import { Modal } from '../components/ui/Modal';
import '../styles/modal.css';

const EMPTY_FORM = { name: '', description: '', imageUrl: '', orderIndex: 0 };

const formFromCategory = (category) => ({
  name: category.name || '',
  description: category.description || '',
  imageUrl: category.imageUrl || '',
  orderIndex: category.orderIndex ?? 0,
});

const validateCategoryForm = (form) => {
  const name = form.name.trim();
  if (name.length < 2) return 'Tên danh mục phải có ít nhất 2 ký tự.';
  if (name.length > 100) return 'Tên danh mục không được vượt quá 100 ký tự.';
  if (form.imageUrl.trim() && !/^https?:\/\//i.test(form.imageUrl.trim())) {
    return 'URL hình ảnh phải bắt đầu bằng http:// hoặc https://';
  }
  if (form.orderIndex !== '' && Number(form.orderIndex) < 0) {
    return 'Thứ tự hiển thị phải là số không âm.';
  }
  return null;
};

export const CategoryManagePage = () => {
  const { isAdmin } = useAuth();

  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const [editorOpen, setEditorOpen] = useState(false);
  const [editingCategory, setEditingCategory] = useState(null);
  const [form, setForm] = useState(EMPTY_FORM);
  const [formError, setFormError] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  const [deleteTarget, setDeleteTarget] = useState(null);
  const [deleting, setDeleting] = useState(false);

  const fetchCategories = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const data = await api.get('/categories');
      setCategories(data || []);
    } catch (err) {
      setError(err.message || 'Không thể tải danh sách danh mục.');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchCategories();
  }, [fetchCategories]);

  const stats = useMemo(() => {
    const totalRecipes = categories.reduce((sum, category) => sum + (category.recipeCount || 0), 0);
    const busiest = categories.reduce(
      (best, category) => ((category.recipeCount || 0) > (best?.recipeCount || 0) ? category : best),
      null,
    );
    return { totalRecipes, busiest };
  }, [categories]);

  const openCreateModal = () => {
    setEditingCategory(null);
    setForm(EMPTY_FORM);
    setFormError(null);
    setEditorOpen(true);
  };

  const openEditModal = (category) => {
    setEditingCategory(category);
    setForm(formFromCategory(category));
    setFormError(null);
    setEditorOpen(true);
  };

  const closeEditor = () => {
    if (submitting) return;
    setEditorOpen(false);
    setEditingCategory(null);
    setFormError(null);
  };

  const handleFormChange = (event) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const validationError = validateCategoryForm(form);
    if (validationError) {
      setFormError(validationError);
      return;
    }

    setSubmitting(true);
    setFormError(null);

    const payload = {
      name: form.name.trim(),
      description: form.description.trim() || null,
      imageUrl: form.imageUrl.trim() || null,
      orderIndex: form.orderIndex === '' ? 0 : Number(form.orderIndex),
    };

    try {
      if (editingCategory) {
        await api.put(`/categories/${editingCategory.id}`, payload);
        setSuccess(`Đã cập nhật danh mục "${payload.name}".`);
      } else {
        await api.post('/categories', payload);
        setSuccess(`Đã thêm danh mục "${payload.name}".`);
      }

      setEditorOpen(false);
      setEditingCategory(null);
      await fetchCategories();
    } catch (err) {
      setFormError(err.message || 'Không thể lưu danh mục.');
    } finally {
      setSubmitting(false);
    }
  };

  const handleDelete = async () => {
    if (!deleteTarget) return;

    setDeleting(true);
    setError(null);

    try {
      await api.delete(`/categories/${deleteTarget.id}`);
      setSuccess(`Đã xóa danh mục "${deleteTarget.name}".`);
      setDeleteTarget(null);
      await fetchCategories();
    } catch (err) {
      setError(err.message || 'Không thể xóa danh mục.');
      setDeleteTarget(null);
    } finally {
      setDeleting(false);
    }
  };

  if (!isAdmin) {
    return (
      <div className="container" style={{ padding: '6rem 1.25rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '1.5rem', marginBottom: '0.75rem' }}>Không có quyền truy cập</h1>
        <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
          Chỉ quản trị viên mới có thể quản lý danh mục ẩm thực.
        </p>
        <Link to="/dashboard" className="btn btn-primary btn-sm">Quay lại bảng điều khiển</Link>
      </div>
    );
  }

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 6rem', maxWidth: '1060px' }}>
      <div style={{ marginBottom: '2rem' }}>
        <Link
          to="/dashboard"
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
          <span>Quay lại bảng điều khiển</span>
        </Link>

        <div className="admin-toolbar" style={{ marginBottom: 0 }}>
          <div>
            <h1 style={{ fontSize: '1.875rem', marginBottom: '0.25rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <FolderTree size={24} style={{ color: 'var(--primary)' }} />
              Quản Lý Danh Mục
            </h1>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
              Tạo, chỉnh sửa và sắp xếp danh mục dùng chung cho toàn hệ thống.
            </p>
          </div>

          <button type="button" className="btn btn-primary" onClick={openCreateModal}>
            <Plus size={16} />
            <span>Thêm danh mục</span>
          </button>
        </div>
      </div>

      {error && (
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <AlertCircle size={16} />
          <span>{error}</span>
        </div>
      )}

      {success && (
        <div className="alert alert-success" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }} role="status">
          <CheckCircle size={16} />
          <span>{success}</span>
        </div>
      )}

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '1rem', marginBottom: '1.5rem' }}>
        <div className="admin-stat">
          <span className="admin-stat-value">{categories.length}</span>
          <span className="admin-stat-label">Danh mục</span>
        </div>
        <div className="admin-stat">
          <span className="admin-stat-value">{stats.totalRecipes}</span>
          <span className="admin-stat-label">Công thức đã xuất bản</span>
        </div>
        <div className="admin-stat">
          <span className="admin-stat-value" style={{ fontSize: '1.125rem' }}>{stats.busiest?.name || '—'}</span>
          <span className="admin-stat-label">Danh mục nhiều món nhất</span>
        </div>
      </div>

      <div className="card" style={{ overflow: 'hidden' }}>
        <div
          style={{
            padding: '1.25rem 1.5rem',
            borderBottom: '1px solid var(--border)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <h2 style={{ fontSize: '1.125rem' }}>Danh Sách Danh Mục</h2>
          <button type="button" className="btn btn-outline btn-sm" onClick={fetchCategories} title="Làm mới">
            <RefreshCw size={14} />
            <span>Làm mới</span>
          </button>
        </div>

        {loading ? (
          <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>Đang tải danh mục...</div>
        ) : categories.length === 0 ? (
          <div style={{ padding: '3rem 1rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            Chưa có danh mục nào. Hãy thêm danh mục đầu tiên.
          </div>
        ) : (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.875rem' }}>
              <thead>
                <tr
                  style={{
                    backgroundColor: '#f8fafc',
                    borderBottom: '1px solid var(--border)',
                    color: 'var(--text-muted)',
                    fontSize: '0.75rem',
                    textTransform: 'uppercase',
                  }}
                >
                  <th style={{ padding: '0.75rem 1.25rem' }}>Danh mục</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Slug</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Thứ tự</th>
                  <th style={{ padding: '0.75rem 1rem' }}>Công thức</th>
                  <th style={{ padding: '0.75rem 1.25rem', textAlign: 'right' }}>Thao tác</th>
                </tr>
              </thead>
              <tbody>
                {categories.map((category) => (
                  <tr key={category.id} style={{ borderBottom: '1px solid var(--border)' }}>
                    <td style={{ padding: '0.875rem 1.25rem' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                        {category.imageUrl ? (
                          <img
                            src={category.imageUrl}
                            alt={category.name}
                            style={{ width: '2.5rem', height: '2.5rem', borderRadius: '0.5rem', objectFit: 'cover' }}
                          />
                        ) : (
                          <div
                            style={{
                              width: '2.5rem',
                              height: '2.5rem',
                              borderRadius: '0.5rem',
                              backgroundColor: 'var(--primary-light)',
                              color: 'var(--primary)',
                              display: 'flex',
                              alignItems: 'center',
                              justifyContent: 'center',
                            }}
                          >
                            <Tag size={16} />
                          </div>
                        )}
                        <div>
                          <div className="admin-category-name">{category.name}</div>
                          {category.description && (
                            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: 2 }}>
                              {category.description}
                            </div>
                          )}
                        </div>
                      </div>
                    </td>

                    <td style={{ padding: '0.875rem 1rem', color: 'var(--text-muted)', fontSize: '0.8125rem' }}>
                      {category.slug}
                    </td>

                    <td style={{ padding: '0.875rem 1rem' }}>{category.orderIndex ?? 0}</td>

                    <td style={{ padding: '0.875rem 1rem' }}>
                      <span className="badge badge-draft">{category.recipeCount || 0} món</span>
                    </td>

                    <td style={{ padding: '0.875rem 1.25rem', textAlign: 'right' }}>
                      <div style={{ display: 'inline-flex', gap: '0.375rem' }}>
                        <button
                          type="button"
                          className="btn btn-outline btn-sm"
                          onClick={() => openEditModal(category)}
                          title="Chỉnh sửa danh mục"
                        >
                          <Edit2 size={14} />
                          <span>Sửa</span>
                        </button>
                        <button
                          type="button"
                          className="btn btn-sm"
                          style={{ backgroundColor: '#fef2f2', color: '#dc2626' }}
                          onClick={() => setDeleteTarget(category)}
                          title="Xóa danh mục"
                        >
                          <Trash2 size={14} />
                          <span>Xóa</span>
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      <Modal
        open={editorOpen}
        onClose={closeEditor}
        title={editingCategory ? 'Chỉnh Sửa Danh Mục' : 'Thêm Danh Mục Mới'}
        description={
          editingCategory
            ? 'Cập nhật tên, mô tả và thứ tự hiển thị của danh mục.'
            : 'Danh mục mới sẽ hiển thị ngay trên toàn hệ thống sau khi tạo.'
        }
        footer={
          <>
            <button type="button" className="btn btn-outline" onClick={closeEditor} disabled={submitting}>
              Hủy
            </button>
            <button
              type="submit"
              form="category-form"
              className="btn btn-primary"
              disabled={submitting}
            >
              {submitting ? 'Đang lưu...' : editingCategory ? 'Lưu thay đổi' : 'Tạo danh mục'}
            </button>
          </>
        }
      >
        <form id="category-form" onSubmit={handleSubmit}>
          {formError && (
            <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <AlertCircle size={16} />
              <span>{formError}</span>
            </div>
          )}

          <div className="field">
            <label className="field-label" htmlFor="category-name">Tên danh mục *</label>
            <input
              id="category-name"
              name="name"
              type="text"
              className="input"
              placeholder="VD: Món Chay Thanh Đạm"
              value={form.name}
              onChange={handleFormChange}
              autoFocus
              required
            />
            <span className="field-hint">Từ 2 đến 100 ký tự, dùng để tạo slug tự động.</span>
          </div>

          <div className="field">
            <label className="field-label" htmlFor="category-description">Mô tả</label>
            <textarea
              id="category-description"
              name="description"
              rows={3}
              className="textarea"
              placeholder="Mô tả đặc điểm hoặc các món ăn trong danh mục này..."
              value={form.description}
              onChange={handleFormChange}
            />
          </div>

          <div className="field">
            <label className="field-label" htmlFor="category-image">URL hình ảnh (tùy chọn)</label>
            <input
              id="category-image"
              name="imageUrl"
              type="url"
              className="input"
              placeholder="https://..."
              value={form.imageUrl}
              onChange={handleFormChange}
            />
          </div>

          <div className="field">
            <label className="field-label" htmlFor="category-order">Thứ tự hiển thị</label>
            <input
              id="category-order"
              name="orderIndex"
              type="number"
              min="0"
              className="input admin-order-input"
              value={form.orderIndex}
              onChange={handleFormChange}
            />
            <span className="field-hint">Số nhỏ hơn sẽ hiển thị trước.</span>
          </div>
        </form>
      </Modal>

      <Modal
        open={Boolean(deleteTarget)}
        onClose={() => (deleting ? null : setDeleteTarget(null))}
        title="Xóa Danh Mục"
        description="Hành động này không thể hoàn tác."
        footer={
          <>
            <button
              type="button"
              className="btn btn-outline"
              onClick={() => setDeleteTarget(null)}
              disabled={deleting}
            >
              Hủy
            </button>
            <button type="button" className="btn btn-danger" onClick={handleDelete} disabled={deleting}>
              {deleting ? 'Đang xóa...' : 'Xóa danh mục'}
            </button>
          </>
        }
      >
        <p style={{ fontSize: '0.9375rem', color: 'var(--text-main)' }}>
          Bạn có chắc chắn muốn xóa danh mục <strong>{deleteTarget?.name}</strong>?
        </p>
        {deleteTarget?.recipeCount > 0 && (
          <div className="alert alert-error" style={{ marginTop: '1rem', marginBottom: 0 }}>
            Danh mục này đang chứa {deleteTarget.recipeCount} công thức nên sẽ không thể xóa cho đến khi
            chuyển hoặc xóa hết các công thức đó.
          </div>
        )}
      </Modal>
    </div>
  );
};
