import React, { useState, useEffect, useCallback } from 'react';
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
  AlertTriangle,
  ArrowLeft,
  ChevronLeft,
  ChevronRight,
  FileText,
} from 'lucide-react';

const statusBadge = {
  0: { label: 'Bản nháp', class: 'badge-draft' },
  1: { label: 'Đã xuất bản', class: 'badge-published' },
  2: { label: 'Lưu trữ', class: 'badge-archived' },
};

const STATUS_TABS = [
  { value: null, label: 'Tất cả' },
  { value: 0, label: 'Bản nháp' },
  { value: 1, label: 'Đã xuất bản' },
  { value: 2, label: 'Đã lưu trữ' },
];

const PAGE_SIZE = 10;

export const RecipeManagementPage = () => {
  const { user } = useAuth();
  const [recipes, setRecipes] = useState([]);
  const [meta, setMeta] = useState(null);
  const [page, setPage] = useState(1);
  const [statusFilter, setStatusFilter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [actionError, setActionError] = useState(null);

  const fetchMyRecipes = useCallback(async () => {
    setLoading(true);
    setActionError(null);
    try {
      const params = { mine: true, page, pageSize: PAGE_SIZE };
      if (statusFilter !== null) {
        params.recipeStatus = statusFilter;
      }
      const res = await api.get('/recipes', params);
      setRecipes(res?.items || []);
      setMeta(res?.meta || null);
    } catch (err) {
      console.error('Failed to fetch recipes:', err);
      setActionError(err.message || 'Không thể tải danh sách công thức');
    } finally {
      setLoading(false);
    }
  }, [page, statusFilter]);

  useEffect(() => {
    fetchMyRecipes();
  }, [fetchMyRecipes]);

  const handleStatusTabChange = (value) => {
    setStatusFilter(value);
    setPage(1);
  };

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
        // If we deleted the last item on the current page, go back a page
        if (recipes.length === 1 && page > 1) {
          setPage(page - 1);
        } else {
          fetchMyRecipes();
        }
      } catch (err) {
        setActionError(err.message || 'Không thể xóa công thức');
      }
    }
  };

  const totalPages = meta?.totalPages || 0;
  const totalCount = meta?.total || 0;

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 5rem' }}>

      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <Link to="/dashboard" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.375rem', fontSize: '0.8125rem', color: 'var(--text-muted)', marginBottom: '0.5rem' }}>
            <ArrowLeft size={14} />
            <span>Quay lại Bảng điều khiển</span>
          </Link>
          <h1 style={{ fontSize: '1.75rem', marginBottom: '0.25rem', display: 'flex', alignItems: 'center', gap: '0.625rem' }}>
            <FileText size={26} style={{ color: 'var(--primary)' }} />
            Quản Lý Công Thức
          </h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
            {user?.fullName} — {totalCount} công thức của bạn
          </p>
        </div>

        <Link to="/dashboard/recipes/new" className="btn btn-primary">
          <PlusCircle size={16} />
          <span>Tạo công thức mới</span>
        </Link>
      </div>

      {actionError && (
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1.25rem' }}>
          <AlertTriangle size={16} />
          <span>{actionError}</span>
        </div>
      )}

      {/* Status Filter Tabs */}
      <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1.5rem', flexWrap: 'wrap' }}>
        {STATUS_TABS.map((tab) => (
          <button
            key={String(tab.value)}
            onClick={() => handleStatusTabChange(tab.value)}
            className={statusFilter === tab.value ? 'btn btn-primary btn-sm' : 'btn btn-outline btn-sm'}
          >
            {tab.label}
          </button>
        ))}
      </div>

      {/* Recipes Management Table */}
      <div className="card" style={{ overflow: 'hidden' }}>
        <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2 style={{ fontSize: '1.125rem' }}>Danh Sách Công Thức Của Tôi</h2>
          <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
            {loading ? 'Đang tải...' : `${totalCount} món ăn`}
          </span>
        </div>

        {loading ? (
          <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            Đang tải dữ liệu...
          </div>
        ) : recipes.length > 0 ? (
          <>
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

                            {/* Publish */}
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

                            {/* Unpublish */}
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

            {/* Pagination */}
            {totalPages > 1 && (
              <div style={{ padding: '1rem 1.5rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderTop: '1px solid var(--border)' }}>
                <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
                  Trang {meta.page} / {totalPages}
                </span>
                <div style={{ display: 'flex', gap: '0.5rem' }}>
                  <button
                    onClick={() => setPage(page - 1)}
                    disabled={page <= 1}
                    className="btn btn-outline btn-sm"
                    style={{ opacity: page <= 1 ? 0.5 : 1, cursor: page <= 1 ? 'not-allowed' : 'pointer' }}
                  >
                    <ChevronLeft size={14} />
                    <span>Trước</span>
                  </button>
                  <button
                    onClick={() => setPage(page + 1)}
                    disabled={page >= totalPages}
                    className="btn btn-outline btn-sm"
                    style={{ opacity: page >= totalPages ? 0.5 : 1, cursor: page >= totalPages ? 'not-allowed' : 'pointer' }}
                  >
                    <span>Sau</span>
                    <ChevronRight size={14} />
                  </button>
                </div>
              </div>
            )}
          </>
        ) : (
          <div style={{ padding: '4rem 1rem', textAlign: 'center' }}>
            <p style={{ color: 'var(--text-muted)', marginBottom: '1.25rem' }}>
              {statusFilter !== null
                ? 'Không có công thức nào với trạng thái này.'
                : 'Bạn chưa có công thức nào.'}
            </p>
            <Link to="/dashboard/recipes/new" className="btn btn-primary btn-sm">
              Tạo công thức đầu tiên
            </Link>
          </div>
        )}
      </div>

    </div>
  );
};
