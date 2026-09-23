import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import {
  PlusCircle,
  Eye,
  Edit,
  Trash2,
  CheckCircle,
  Archive,
  Clock,
  Flame,
  AlertTriangle,
} from 'lucide-react';

const statusBadge = {
  0: { label: 'Bản nháp', class: 'badge-draft' },
  1: { label: 'Đã xuất bản', class: 'badge-published' },
  2: { label: 'Lưu trữ', class: 'badge-archived' },
};

export const CreatorDashboard = () => {
  const { user } = useAuth();
  const [recipes, setRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionError, setActionError] = useState(null);

  const fetchMyRecipes = async () => {
    setLoading(true);
    setActionError(null);
    try {
      // Get all recipes including drafts & archived for current author
      const res = await api.get('/recipes', { pageSize: 50 });
      setRecipes(res?.items || []);
    } catch (err) {
      console.error('Failed to fetch recipes:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMyRecipes();
  }, []);

  const handlePublish = async (id) => {
    try {
      await api.patch(`/recipes/${id}/publish`);
      fetchMyRecipes();
    } catch (err) {
      setActionError(err.message || 'Không thể xuất bản công thức');
    }
  };

  const handleUnpublish = async (id) => {
    try {
      await api.patch(`/recipes/${id}/unpublish`);
      fetchMyRecipes();
    } catch (err) {
      setActionError(err.message || 'Không thể hủy xuất bản');
    }
  };

  const handleArchive = async (id) => {
    try {
      await api.patch(`/recipes/${id}/archive`);
      fetchMyRecipes();
    } catch (err) {
      setActionError(err.message || 'Không thể lưu trữ');
    }
  };

  const handleDelete = async (id, title) => {
    if (window.confirm(`Bạn có chắc chắn muốn xóa công thức "${title}" không? Hành động này không thể hoàn tác.`)) {
      try {
        await api.delete(`/recipes/${id}`);
        fetchMyRecipes();
      } catch (err) {
        setActionError(err.message || 'Không thể xóa công thức');
      }
    }
  };

  const totalCount = recipes.length;
  const publishedCount = recipes.filter((r) => r.status === 1).length;
  const draftCount = recipes.filter((r) => r.status === 0).length;
  const archivedCount = recipes.filter((r) => r.status === 2).length;

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 5rem' }}>
      
      {/* Top Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2.5rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <h1 style={{ fontSize: '2rem', marginBottom: '0.25rem' }}>Bảng Điều Khiển Tác Giả</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
            Xin chào, <strong>{user?.fullName}</strong>! Quản lý các công thức nấu ăn của bạn tại đây.
          </p>
        </div>

        <Link to="/dashboard/recipes/new" className="btn btn-primary">
          <PlusCircle size={16} />
          <span>Tạo công thức mới</span>
        </Link>
      </div>

      {actionError && (
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <AlertTriangle size={16} />
          <span>{actionError}</span>
        </div>
      )}

      {/* Stats Summary Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.25rem', marginBottom: '2.5rem' }}>
        <div className="card" style={{ padding: '1.5rem' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
            Tổng số công thức
          </span>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--secondary)', marginTop: '0.25rem' }}>
            {totalCount}
          </div>
        </div>

        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid #059669' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#059669', textTransform: 'uppercase' }}>
            Đã xuất bản (Published)
          </span>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#059669', marginTop: '0.25rem' }}>
            {publishedCount}
          </div>
        </div>

        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid #d97706' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#d97706', textTransform: 'uppercase' }}>
            Bản nháp (Draft)
          </span>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#d97706', marginTop: '0.25rem' }}>
            {draftCount}
          </div>
        </div>

        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid #dc2626' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#dc2626', textTransform: 'uppercase' }}>
            Đã lưu trữ (Archived)
          </span>
          <div style={{ fontSize: '2rem', fontWeight: 800, color: '#dc2626', marginTop: '0.25rem' }}>
            {archivedCount}
          </div>
        </div>
      </div>

      {/* Recipes Management Table */}
      <div className="card" style={{ overflow: 'hidden' }}>
        <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2 style={{ fontSize: '1.25rem' }}>Danh Sách Công Thức Của Tôi</h2>
          <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>{recipes.length} món ăn</span>
        </div>

        {loading ? (
          <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            Đang tải dữ liệu...
          </div>
        ) : recipes.length > 0 ? (
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.875rem' }}>
              <thead>
                <tr style={{ backgroundColor: '#f8fafc', borderBottom: '1px solid var(--border)', color: 'var(--text-muted)', fontSize: '0.75rem', textTransform: 'uppercase' }}>
                  <th style={{ padding: '0.875rem 1.25rem' }}>Món ăn</th>
                  <th style={{ padding: '0.875rem 1rem' }}>Danh mục</th>
                  <th style={{ padding: '0.875rem 1rem' }}>Thời gian</th>
                  <th style={{ padding: '0.875rem 1rem' }}>Trạng thái</th>
                  <th style={{ padding: '0.875rem 1rem' }}>Ngày tạo</th>
                  <th style={{ padding: '0.875rem 1.25rem', textAlign: 'right' }}>Thao tác</th>
                </tr>
              </thead>
              <tbody>
                {recipes.map((r) => {
                  const s = statusBadge[r.status] || statusBadge[0];
                  return (
                    <tr key={r.id} style={{ borderBottom: '1px solid var(--border)' }}>
                      <td style={{ padding: '1rem 1.25rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.875rem' }}>
                          <img
                            src={r.primaryImage?.thumbnailUrl || r.primaryImage?.originalUrl || 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=120&q=80'}
                            alt={r.title}
                            style={{ width: '2.75rem', height: '2.75rem', borderRadius: '0.5rem', objectFit: 'cover' }}
                          />
                          <div>
                            <Link to={`/recipes/${r.slug}`} style={{ fontWeight: 700, color: 'var(--secondary)' }}>
                              {r.title}
                            </Link>
                            <span style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                              /{r.slug}
                            </span>
                          </div>
                        </div>
                      </td>

                      <td style={{ padding: '1rem' }}>
                        <span style={{ fontSize: '0.8125rem' }}>{r.category?.name || '—'}</span>
                      </td>

                      <td style={{ padding: '1rem', whiteSpace: 'nowrap' }}>
                        <span style={{ fontSize: '0.8125rem' }}>{(r.prepTime || 0) + (r.cookTime || 0)} phút</span>
                      </td>

                      <td style={{ padding: '1rem' }}>
                        <span className={`badge ${s.class}`}>{s.label}</span>
                      </td>

                      <td style={{ padding: '1rem', fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
                        {new Date(r.createdAt).toLocaleDateString('vi-VN')}
                      </td>

                      <td style={{ padding: '1rem 1.25rem', textAlign: 'right' }}>
                        <div style={{ display: 'inline-flex', gap: '0.375rem' }}>
                          {/* View */}
                          <Link to={`/recipes/${r.slug}`} className="btn btn-outline btn-sm" title="Xem chi tiết">
                            <Eye size={14} />
                          </Link>

                          {/* Edit */}
                          <Link to={`/dashboard/recipes/${r.id}/edit`} className="btn btn-outline btn-sm" title="Chỉnh sửa">
                            <Edit size={14} />
                          </Link>

                          {/* Publish / Unpublish */}
                          {r.status === 0 && (
                            <button
                              onClick={() => handlePublish(r.id)}
                              className="btn btn-sm"
                              style={{ backgroundColor: '#ecfdf5', color: '#059669' }}
                              title="Xuất bản"
                            >
                              <CheckCircle size={14} />
                            </button>
                          )}

                          {r.status === 1 && (
                            <button
                              onClick={() => handleUnpublish(r.id)}
                              className="btn btn-sm"
                              style={{ backgroundColor: '#fffbeb', color: '#d97706' }}
                              title="Hủy xuất bản về Draft"
                            >
                              <Clock size={14} />
                            </button>
                          )}

                          {/* Archive */}
                          {r.status !== 2 && (
                            <button
                              onClick={() => handleArchive(r.id)}
                              className="btn btn-outline btn-sm"
                              title="Lưu trữ"
                            >
                              <Archive size={14} />
                            </button>
                          )}

                          {/* Delete */}
                          <button
                            onClick={() => handleDelete(r.id, r.title)}
                            className="btn btn-sm"
                            style={{ backgroundColor: '#fef2f2', color: '#dc2626' }}
                            title="Xóa công thức"
                          >
                            <Trash2 size={14} />
                          </button>
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        ) : (
          <div style={{ padding: '4rem 1rem', textAlign: 'center' }}>
            <p style={{ color: 'var(--text-muted)', marginBottom: '1.25rem' }}>Bạn chưa có công thức nào.</p>
            <Link to="/dashboard/recipes/new" className="btn btn-primary btn-sm">
              Tạo công thức đầu tiên
            </Link>
          </div>
        )}
      </div>

    </div>
  );
};
