import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import {
  PlusCircle,
  FileText,
  CheckCircle,
  Clock,
  Archive,
  TrendingUp,
  BookOpen,
  ChefHat,
  AlertTriangle,
} from 'lucide-react';

const statusBadge = {
  0: { label: 'Bản nháp', class: 'badge-draft' },
  1: { label: 'Đã xuất bản', class: 'badge-published' },
  2: { label: 'Lưu trữ', class: 'badge-archived' },
};

export const CreatorDashboard = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        setLoading(true);
        const data = await api.get('/dashboard/stats');
        setStats(data);
      } catch (err) {
        console.error('Failed to fetch dashboard stats:', err);
        setError(err.message || 'Không thể tải thống kê bảng điều khiển');
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  if (loading) {
    return (
      <div className="container" style={{ padding: '4rem 1.25rem', textAlign: 'center' }}>
        <div style={{ color: 'var(--text-muted)' }}>Đang tải bảng điều khiển...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="container" style={{ padding: '4rem 1.25rem' }}>
        <div className="alert alert-error" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <AlertTriangle size={16} />
          <span>{error}</span>
        </div>
      </div>
    );
  }

  const totalRecipes = stats?.totalRecipes || 0;
  const publishedCount = stats?.publishedCount || 0;
  const draftCount = stats?.draftCount || 0;
  const archivedCount = stats?.archivedCount || 0;
  const recentRecipes = stats?.recentRecipes || [];
  const categoryDistribution = stats?.categoryDistribution || [];
  const difficultyDistribution = stats?.difficultyDistribution || [];

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 5rem' }}>
      
      {/* Header */}
      <div style={{ marginBottom: '2.5rem' }}>
        <h1 style={{ fontSize: '2rem', marginBottom: '0.25rem', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <ChefHat size={32} style={{ color: 'var(--primary)' }} />
          Bảng Điều Khiển Tác Giả
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
          Xin chào, <strong>{user?.fullName}</strong>! Đây là tổng quan hoạt động sáng tạo ẩm thực của bạn.
        </p>
      </div>

      {/* Quick Actions */}
      <div className="card" style={{ padding: '1.5rem', marginBottom: '2rem', background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', color: 'white' }}>
        <h3 style={{ fontSize: '1.125rem', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <TrendingUp size={20} />
          Hành động nhanh
        </h3>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <Link to="/dashboard/recipes/new" className="btn" style={{ backgroundColor: 'rgba(255,255,255,0.2)', color: 'white', border: '1px solid rgba(255,255,255,0.3)' }}>
            <PlusCircle size={16} />
            <span>Tạo công thức mới</span>
          </Link>
          <Link to="/dashboard/recipes" className="btn" style={{ backgroundColor: 'rgba(255,255,255,0.2)', color: 'white', border: '1px solid rgba(255,255,255,0.3)' }}>
            <FileText size={16} />
            <span>Quản lý công thức</span>
          </Link>
        </div>
      </div>

      {/* Statistics Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '1.25rem', marginBottom: '2.5rem' }}>
        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid var(--primary)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start' }}>
            <div>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase' }}>
                Tổng số công thức
              </span>
              <div style={{ fontSize: '2.5rem', fontWeight: 800, color: 'var(--primary)', marginTop: '0.25rem' }}>
                {totalRecipes}
              </div>
            </div>
            <BookOpen size={32} style={{ color: 'var(--primary)', opacity: 0.3 }} />
          </div>
        </div>

        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid #059669' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start' }}>
            <div>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#059669', textTransform: 'uppercase' }}>
                Đã xuất bản
              </span>
              <div style={{ fontSize: '2.5rem', fontWeight: 800, color: '#059669', marginTop: '0.25rem' }}>
                {publishedCount}
              </div>
            </div>
            <CheckCircle size={32} style={{ color: '#059669', opacity: 0.3 }} />
          </div>
        </div>

        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid #d97706' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start' }}>
            <div>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#d97706', textTransform: 'uppercase' }}>
                Bản nháp
              </span>
              <div style={{ fontSize: '2.5rem', fontWeight: 800, color: '#d97706', marginTop: '0.25rem' }}>
                {draftCount}
              </div>
            </div>
            <Clock size={32} style={{ color: '#d97706', opacity: 0.3 }} />
          </div>
        </div>

        <div className="card" style={{ padding: '1.5rem', borderLeft: '4px solid #dc2626' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start' }}>
            <div>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#dc2626', textTransform: 'uppercase' }}>
                Đã lưu trữ
              </span>
              <div style={{ fontSize: '2.5rem', fontWeight: 800, color: '#dc2626', marginTop: '0.25rem' }}>
                {archivedCount}
              </div>
            </div>
            <Archive size={32} style={{ color: '#dc2626', opacity: 0.3 }} />
          </div>
        </div>
      </div>

      {/* Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', gap: '1.5rem' }}>
        
        {/* Recent Recipes */}
        <div className="card" style={{ overflow: 'hidden' }}>
          <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)' }}>
            <h2 style={{ fontSize: '1.125rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <Clock size={18} />
              Công thức gần đây
            </h2>
          </div>
          <div style={{ padding: '1rem 1.5rem' }}>
            {recentRecipes.length > 0 ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                {recentRecipes.map((recipe) => (
                  <Link
                    key={recipe.id}
                    to={`/recipes/${recipe.slug}`}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '1rem',
                      padding: '0.75rem',
                      borderRadius: '0.5rem',
                      textDecoration: 'none',
                      transition: 'background-color 0.2s',
                    }}
                    onMouseEnter={(e) => e.currentTarget.style.backgroundColor = '#f8fafc'}
                    onMouseLeave={(e) => e.currentTarget.style.backgroundColor = 'transparent'}
                  >
                    <img
                      src={recipe.primaryImageUrl || 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=120&q=80'}
                      alt={recipe.title}
                      style={{ width: '3.5rem', height: '3.5rem', borderRadius: '0.5rem', objectFit: 'cover' }}
                    />
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <div style={{ fontWeight: 600, color: 'var(--secondary)', marginBottom: '0.25rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                        {recipe.title}
                      </div>
                      <div style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                        <span>{recipe.category}</span>
                        <span>•</span>
                        <span>{new Date(recipe.createdAt).toLocaleDateString('vi-VN')}</span>
                      </div>
                    </div>
                    <span className={`badge ${statusBadge[recipe.status]?.class || 'badge-draft'}`}>
                      {statusBadge[recipe.status]?.label}
                    </span>
                  </Link>
                ))}
              </div>
            ) : (
              <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                Bạn chưa có công thức nào. Bắt đầu tạo công thức đầu tiên!
              </div>
            )}
          </div>
        </div>

        {/* Category Distribution */}
        <div className="card" style={{ overflow: 'hidden' }}>
          <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)' }}>
            <h2 style={{ fontSize: '1.125rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <BookOpen size={18} />
              Phân bố theo danh mục
            </h2>
          </div>
          <div style={{ padding: '1.5rem' }}>
            {categoryDistribution.length > 0 ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.875rem' }}>
                {categoryDistribution.map((cat) => {
                  const percentage = totalRecipes > 0 ? (cat.recipeCount / totalRecipes) * 100 : 0;
                  return (
                    <div key={cat.categoryId}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem', fontSize: '0.875rem' }}>
                        <span style={{ fontWeight: 600 }}>{cat.categoryName}</span>
                        <span style={{ color: 'var(--text-muted)' }}>
                          {cat.recipeCount} công thức ({percentage.toFixed(1)}%)
                        </span>
                      </div>
                      <div style={{ height: '8px', backgroundColor: '#f1f5f9', borderRadius: '4px', overflow: 'hidden' }}>
                        <div
                          style={{
                            height: '100%',
                            width: `${percentage}%`,
                            backgroundColor: 'var(--primary)',
                            borderRadius: '4px',
                            transition: 'width 0.3s ease',
                          }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            ) : (
              <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                Chưa có dữ liệu danh mục
              </div>
            )}
          </div>
        </div>

        {/* Difficulty Distribution */}
        <div className="card" style={{ overflow: 'hidden' }}>
          <div style={{ padding: '1.25rem 1.5rem', borderBottom: '1px solid var(--border)' }}>
            <h2 style={{ fontSize: '1.125rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <TrendingUp size={18} />
              Phân bố theo độ khó
            </h2>
          </div>
          <div style={{ padding: '1.5rem' }}>
            {difficultyDistribution.length > 0 ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.875rem' }}>
                {difficultyDistribution.map((diff) => {
                  const percentage = totalRecipes > 0 ? (diff.count / totalRecipes) * 100 : 0;
                  const colors = {
                    1: '#10b981', // Easy - green
                    2: '#f59e0b', // Medium - amber
                    3: '#ef4444', // Hard - red
                    4: '#8b5cf6', // Expert - purple
                  };
                  return (
                    <div key={diff.difficulty}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem', fontSize: '0.875rem' }}>
                        <span style={{ fontWeight: 600 }}>{diff.difficultyLabel}</span>
                        <span style={{ color: 'var(--text-muted)' }}>
                          {diff.count} công thức ({percentage.toFixed(1)}%)
                        </span>
                      </div>
                      <div style={{ height: '8px', backgroundColor: '#f1f5f9', borderRadius: '4px', overflow: 'hidden' }}>
                        <div
                          style={{
                            height: '100%',
                            width: `${percentage}%`,
                            backgroundColor: colors[diff.difficulty] || '#6b7280',
                            borderRadius: '4px',
                            transition: 'width 0.3s ease',
                          }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            ) : (
              <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-muted)' }}>
                Chưa có dữ liệu độ khó
              </div>
            )}
          </div>
        </div>

      </div>

    </div>
  );
};
