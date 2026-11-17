import React, { useState, useEffect } from 'react';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import {
  Users,
  Search,
  Shield,
  UserCheck,
  UserX,
  BookOpen,
  Calendar,
  AlertCircle,
  CheckCircle,
  RefreshCw,
  Mail,
  ChevronLeft,
  ChevronRight,
} from 'lucide-react';

export const UsersPage = () => {
  const { user: currentUser } = useAuth();
  const isAdmin = currentUser?.roles?.includes('Admin') || currentUser?.role === 'Admin';

  const [users, setUsers] = useState([]);
  const [meta, setMeta] = useState({
    page: 1,
    pageSize: 10,
    totalCount: 0,
    totalPages: 1,
    hasNextPage: false,
    hasPreviousPage: false,
  });

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  // Filters
  const [page, setPage] = useState(1);
  const [search, setSearch] = useState('');
  const [searchDebounce, setSearchDebounce] = useState('');
  const [roleFilter, setRoleFilter] = useState('ALL');
  const [updatingId, setUpdatingId] = useState(null);

  // Debounce search
  useEffect(() => {
    const handler = setTimeout(() => {
      setSearchDebounce(search);
      setPage(1);
    }, 400);
    return () => clearTimeout(handler);
  }, [search]);

  const fetchUsers = async () => {
    setLoading(true);
    setError(null);
    try {
      const params = new URLSearchParams();
      params.append('page', page);
      params.append('pageSize', '10');
      if (roleFilter !== 'ALL') {
        params.append('role', roleFilter);
      }
      if (searchDebounce.trim()) {
        params.append('search', searchDebounce.trim());
      }

      const res = await api.get(`/users?${params.toString()}`);
      if (res && res.items) {
        setUsers(res.items);
        setMeta(res.meta);
      } else {
        setUsers([]);
      }
    } catch (err) {
      setError(err.message || 'Không thể tải danh sách người dùng.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, [page, roleFilter, searchDebounce]);

  // Handle role update
  const handleRoleChange = async (userId, newRole) => {
    if (!isAdmin) return;
    setUpdatingId(userId);
    setError(null);
    setSuccess(null);
    try {
      await api.patch(`/users/${userId}/role`, { role: newRole });
      setSuccess(`Đã cập nhật vai trò người dùng thành "${newRole}" thành công!`);
      fetchUsers();
    } catch (err) {
      setError(err.message || 'Không thể thay đổi vai trò.');
    } finally {
      setUpdatingId(null);
    }
  };

  // Handle status toggle (Lock / Unlock)
  const handleToggleStatus = async (userObj) => {
    if (!isAdmin) return;
    setUpdatingId(userObj.id);
    setError(null);
    setSuccess(null);
    try {
      await api.patch(`/users/${userObj.id}/status`, { isActive: !userObj.isActive });
      setSuccess(
        userObj.isActive
          ? `Đã khóa tài khoản "${userObj.fullName}" thành công!`
          : `Đã mở khóa tài khoản "${userObj.fullName}" thành công!`
      );
      fetchUsers();
    } catch (err) {
      setError(err.message || 'Không thể thay đổi trạng thái tài khoản.');
    } finally {
      setUpdatingId(null);
    }
  };

  const getRoleBadge = (role) => {
    switch (role?.toLowerCase()) {
      case 'admin':
        return {
          label: 'Quản trị viên (Admin)',
          bg: '#fee2e2',
          color: '#b91c1c',
          border: '#fca5a5',
        };
      case 'author':
        return {
          label: 'Tác giả (Author)',
          bg: '#fef3c7',
          color: '#b45309',
          border: '#fcd34d',
        };
      default:
        return {
          label: 'Thành viên (User)',
          bg: '#e0f2fe',
          color: '#0369a1',
          border: '#bae6fd',
        };
    }
  };

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 6rem', maxWidth: '1100px' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.625rem' }}>
            <div style={{ padding: '0.625rem', backgroundColor: 'var(--primary-bg, #fff5ed)', borderRadius: '0.75rem', color: 'var(--primary, #ea580c)' }}>
              <Users size={26} />
            </div>
            <div>
              <h1 style={{ fontSize: '1.75rem', fontWeight: 800, margin: 0, color: 'var(--text-main, #1e293b)' }}>
                Danh Sách Người Dùng & Tác Giả
              </h1>
              <p style={{ margin: 0, color: 'var(--text-muted, #64748b)', fontSize: '0.875rem' }}>
                Quản lý thông tin tài khoản, phân quyền tác giả và quản trị viên hệ thống
              </p>
            </div>
          </div>
        </div>

        <button
          onClick={fetchUsers}
          className="btn btn-outline btn-sm"
          disabled={loading}
          style={{ display: 'flex', alignItems: 'center', gap: '0.375rem' }}
        >
          <RefreshCw size={14} className={loading ? 'animate-spin' : ''} />
          <span>Làm mới</span>
        </button>
      </div>

      {/* Alerts */}
      {error && (
        <div style={{ padding: '0.875rem 1.25rem', backgroundColor: '#fee2e2', color: '#b91c1c', borderRadius: '0.5rem', marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem', border: '1px solid #fecaca' }}>
          <AlertCircle size={18} />
          <span>{error}</span>
        </div>
      )}
      {success && (
        <div style={{ padding: '0.875rem 1.25rem', backgroundColor: '#dcfce7', color: '#15803d', borderRadius: '0.5rem', marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem', border: '1px solid #bbf7d0' }}>
          <CheckCircle size={18} />
          <span>{success}</span>
        </div>
      )}

      {/* Filter and Search Bar */}
      <div className="card" style={{ padding: '1.25rem 1.5rem', marginBottom: '1.5rem', display: 'flex', flexWrap: 'wrap', gap: '1rem', alignItems: 'center', justifyContent: 'space-between' }}>
        {/* Search */}
        <div style={{ position: 'relative', flex: '1 1 280px', minWidth: '240px' }}>
          <Search size={16} style={{ position: 'absolute', left: '0.875rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
          <input
            type="text"
            className="form-control"
            placeholder="Tìm theo họ tên, username, email..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{ paddingLeft: '2.5rem' }}
          />
        </div>

        {/* Role Filter Tabs */}
        <div style={{ display: 'flex', gap: '0.375rem', flexWrap: 'wrap' }}>
          {[
            { id: 'ALL', label: 'Tất cả vai trò' },
            { id: 'Admin', label: 'Quản trị viên' },
            { id: 'Author', label: 'Tác giả' },
            { id: 'User', label: 'Thành viên' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => {
                setRoleFilter(tab.id);
                setPage(1);
              }}
              className={`btn btn-sm ${roleFilter === tab.id ? 'btn-primary' : 'btn-outline'}`}
              style={{ padding: '0.4rem 0.875rem', fontSize: '0.8125rem' }}
            >
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* User Table Card */}
      <div className="card" style={{ padding: '0', overflow: 'hidden' }}>
        <div style={{ overflowX: 'auto' }}>
          <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.875rem' }}>
            <thead>
              <tr style={{ backgroundColor: 'var(--table-header-bg, #f8fafc)', borderBottom: '1px solid var(--border, #e2e8f0)', color: 'var(--text-muted, #64748b)' }}>
                <th style={{ padding: '1rem 1.25rem', fontWeight: 600 }}>Người dùng</th>
                <th style={{ padding: '1rem 1.25rem', fontWeight: 600 }}>Email & Liên hệ</th>
                <th style={{ padding: '1rem 1.25rem', fontWeight: 600 }}>Vai trò</th>
                <th style={{ padding: '1rem 1.25rem', fontWeight: 600 }}>Công thức</th>
                <th style={{ padding: '1rem 1.25rem', fontWeight: 600 }}>Trạng thái</th>
                <th style={{ padding: '1rem 1.25rem', fontWeight: 600 }}>Ngày tham gia</th>
                {isAdmin && <th style={{ padding: '1rem 1.25rem', fontWeight: 600, textAlign: 'right' }}>Thao tác Admin</th>}
              </tr>
            </thead>
            <tbody>
              {loading && users.length === 0 ? (
                <tr>
                  <td colSpan={isAdmin ? 7 : 6} style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                    Đang tải danh sách người dùng...
                  </td>
                </tr>
              ) : users.length === 0 ? (
                <tr>
                  <td colSpan={isAdmin ? 7 : 6} style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                    Không tìm thấy người dùng phù hợp với tiêu chí lọc.
                  </td>
                </tr>
              ) : (
                users.map((u) => {
                  const roleStyle = getRoleBadge(u.role);
                  return (
                    <tr key={u.id} style={{ borderBottom: '1px solid var(--border, #e2e8f0)', transition: 'background-color 0.15s' }}>
                      {/* Name & Avatar */}
                      <td style={{ padding: '1rem 1.25rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                          <img
                            src={u.avatarUrl || `https://ui-avatars.com/api/?name=${encodeURIComponent(u.fullName || 'User')}&background=ea580c&color=fff`}
                            alt={u.fullName}
                            style={{ width: '38px', height: '38px', borderRadius: '50%', objectFit: 'cover' }}
                          />
                          <div>
                            <div style={{ fontWeight: 600, color: 'var(--text-main, #0f172a)' }}>
                              {u.fullName}
                            </div>
                            <div style={{ fontSize: '0.75rem', color: 'var(--text-muted, #64748b)' }}>
                              @{u.userName}
                            </div>
                          </div>
                        </div>
                      </td>

                      {/* Email */}
                      <td style={{ padding: '1rem 1.25rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', color: 'var(--text-muted, #475569)' }}>
                          <Mail size={14} />
                          <span>{u.email}</span>
                        </div>
                      </td>

                      {/* Role Badge */}
                      <td style={{ padding: '1rem 1.25rem' }}>
                        <span
                          style={{
                            display: 'inline-block',
                            padding: '0.25rem 0.625rem',
                            borderRadius: '9999px',
                            fontSize: '0.75rem',
                            fontWeight: 700,
                            backgroundColor: roleStyle.bg,
                            color: roleStyle.color,
                            border: `1px solid ${roleStyle.border}`,
                          }}
                        >
                          {roleStyle.label}
                        </span>
                      </td>

                      {/* Recipe Count */}
                      <td style={{ padding: '1rem 1.25rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', fontWeight: 600, color: 'var(--text-main)' }}>
                          <BookOpen size={15} color="var(--primary)" />
                          <span>{u.recipeCount} bài</span>
                        </div>
                      </td>

                      {/* Status */}
                      <td style={{ padding: '1rem 1.25rem' }}>
                        {u.isActive ? (
                          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.25rem', color: '#15803d', fontWeight: 600, fontSize: '0.75rem' }}>
                            <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#22c55e' }}></span>
                            Hoạt động
                          </span>
                        ) : (
                          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.25rem', color: '#b91c1c', fontWeight: 600, fontSize: '0.75rem' }}>
                            <span style={{ width: '6px', height: '6px', borderRadius: '50%', backgroundColor: '#ef4444' }}></span>
                            Đã khóa
                          </span>
                        )}
                      </td>

                      {/* Created At */}
                      <td style={{ padding: '1rem 1.25rem', color: 'var(--text-muted, #64748b)', fontSize: '0.8125rem' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                          <Calendar size={13} />
                          <span>{new Date(u.createdAt).toLocaleDateString('vi-VN')}</span>
                        </div>
                      </td>

                      {/* Admin Actions */}
                      {isAdmin && (
                        <td style={{ padding: '1rem 1.25rem', textAlign: 'right' }}>
                          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '0.5rem', alignItems: 'center' }}>
                            {/* Role Select */}
                            <select
                              value={u.role || 'Author'}
                              disabled={updatingId === u.id || u.id === currentUser?.id}
                              onChange={(e) => handleRoleChange(u.id, e.target.value)}
                              style={{
                                padding: '0.25rem 0.5rem',
                                fontSize: '0.75rem',
                                borderRadius: '0.375rem',
                                border: '1px solid var(--border)',
                                cursor: 'pointer',
                              }}
                            >
                              <option value="Admin">Admin</option>
                              <option value="Author">Author</option>
                              <option value="User">User</option>
                            </select>

                            {/* Lock / Unlock Button */}
                            {u.id !== currentUser?.id && (
                              <button
                                onClick={() => handleToggleStatus(u)}
                                disabled={updatingId === u.id}
                                className="btn btn-sm"
                                style={{
                                  padding: '0.25rem 0.5rem',
                                  fontSize: '0.75rem',
                                  backgroundColor: u.isActive ? '#fee2e2' : '#dcfce7',
                                  color: u.isActive ? '#b91c1c' : '#15803d',
                                }}
                                title={u.isActive ? 'Khóa tài khoản này' : 'Mở khóa tài khoản này'}
                              >
                                {u.isActive ? <UserX size={14} /> : <UserCheck size={14} />}
                              </button>
                            )}
                          </div>
                        </td>
                      )}
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination Bar */}
        {meta.totalPages > 1 && (
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem 1.5rem', borderTop: '1px solid var(--border, #e2e8f0)', fontSize: '0.875rem' }}>
            <span style={{ color: 'var(--text-muted)' }}>
              Trang {meta.page} / {meta.totalPages} (Tổng cộng {meta.totalCount} người dùng)
            </span>
            <div style={{ display: 'flex', gap: '0.5rem' }}>
              <button
                className="btn btn-outline btn-sm"
                disabled={!meta.hasPreviousPage || loading}
                onClick={() => setPage((p) => Math.max(1, p - 1))}
              >
                <ChevronLeft size={16} /> Trước
              </button>
              <button
                className="btn btn-outline btn-sm"
                disabled={!meta.hasNextPage || loading}
                onClick={() => setPage((p) => p + 1)}
              >
                Sau <ChevronRight size={16} />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

