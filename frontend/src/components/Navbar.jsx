import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
  UtensilsCrossed,
  Search,
  PlusCircle,
  User,
  LogOut,
  LayoutDashboard,
  FolderTree,
  Menu,
  X,
} from 'lucide-react';

export const Navbar = () => {
  const { user, isAuthenticated, isAdmin, logout } = useAuth();
  const [keyword, setKeyword] = useState('');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (keyword.trim()) {
      navigate(`/recipes?q=${encodeURIComponent(keyword.trim())}`);
      setKeyword('');
      setMobileMenuOpen(false);
    }
  };

  return (
    <nav style={{ backgroundColor: '#ffffff', borderBottom: '1px solid var(--border)', position: 'sticky', top: 0, zIndex: 50 }}>
      <div className="container" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', height: '4.5rem' }}>
        
        {/* Brand Logo */}
        <Link to="/" style={{ display: 'flex', alignItems: 'center', gap: '0.625rem', textDecoration: 'none' }}>
          <div style={{
            width: '2.5rem',
            height: '2.5rem',
            backgroundColor: 'var(--primary)',
            borderRadius: '0.75rem',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#ffffff',
            boxShadow: '0 4px 10px rgba(249, 115, 22, 0.3)'
          }}>
            <UtensilsCrossed size={22} />
          </div>
          <div>
            <span style={{ fontSize: '1.25rem', fontWeight: 800, color: 'var(--secondary)', letterSpacing: '-0.025em' }}>
              Culinary<span style={{ color: 'var(--primary)' }}>Blog</span>
            </span>
            <span style={{ display: 'block', fontSize: '0.625rem', fontWeight: 600, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Nhóm 25
            </span>
          </div>
        </Link>

        {/* Search Bar - Desktop */}
        <form onSubmit={handleSearch} style={{ display: 'none', position: 'relative', width: '22rem', maxWidth: '100%' }} className="desktop-search">
          <input
            type="text"
            placeholder="Tìm kiếm công thức, nguyên liệu..."
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            className="input"
            style={{ paddingLeft: '2.5rem', borderRadius: '9999px', fontSize: '0.8125rem' }}
          />
          <Search size={16} style={{ position: 'absolute', left: '0.875rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
        </form>

        {/* Desktop Navigation Links */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
          <Link to="/" style={{ fontWeight: 600, fontSize: '0.875rem', color: 'var(--secondary)' }}>
            Trang chủ
          </Link>
          <Link to="/recipes" style={{ fontWeight: 600, fontSize: '0.875rem', color: 'var(--secondary)' }}>
            Công thức
          </Link>
          <Link to="/categories" style={{ fontWeight: 600, fontSize: '0.875rem', color: 'var(--secondary)' }}>
            Danh mục
          </Link>

          {/* Action buttons */}
          {isAuthenticated ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.875rem', position: 'relative' }}>
              <Link to="/dashboard/recipes/new" className="btn btn-primary btn-sm">
                <PlusCircle size={15} />
                <span>Đăng công thức</span>
              </Link>

              {/* User Dropdown trigger */}
              <div style={{ position: 'relative' }}>
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    padding: '0.375rem 0.625rem',
                    borderRadius: '9999px',
                    border: '1px solid var(--border)',
                    backgroundColor: '#ffffff'
                  }}
                >
                  <div style={{
                    width: '1.75rem',
                    height: '1.75rem',
                    borderRadius: '50%',
                    backgroundColor: 'var(--primary-light)',
                    color: 'var(--primary)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 700,
                    fontSize: '0.75rem'
                  }}>
                    {user?.fullName?.charAt(0).toUpperCase() || 'U'}
                  </div>
                  <span style={{ fontSize: '0.8125rem', fontWeight: 600, maxWidth: '6rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                    {user?.fullName}
                  </span>
                </button>

                {/* Dropdown Menu */}
                {dropdownOpen && (
                  <div
                    style={{
                      position: 'absolute',
                      right: 0,
                      top: '110%',
                      width: '13rem',
                      backgroundColor: '#ffffff',
                      borderRadius: '0.75rem',
                      boxShadow: '0 10px 25px rgba(0,0,0,0.1)',
                      border: '1px solid var(--border)',
                      padding: '0.5rem',
                      zIndex: 100,
                    }}
                    onClick={() => setDropdownOpen(false)}
                  >
                    <div style={{ padding: '0.5rem 0.75rem', borderBottom: '1px solid var(--border)', marginBottom: '0.375rem' }}>
                      <p style={{ fontWeight: 700, fontSize: '0.8125rem' }}>{user?.fullName}</p>
                      <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{user?.email}</p>
                      <span className="badge badge-published" style={{ marginTop: '0.25rem', fontSize: '0.625rem' }}>
                        {user?.roles?.[0] || 'Author'}
                      </span>
                    </div>

                    <Link to="/dashboard" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.5rem 0.75rem', fontSize: '0.8125rem', borderRadius: '0.375rem' }} className="menu-item">
                      <LayoutDashboard size={15} />
                      <span>Bảng điều khiển</span>
                    </Link>

                    {isAdmin && (
                      <Link to="/dashboard/categories" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.5rem 0.75rem', fontSize: '0.8125rem', borderRadius: '0.375rem' }} className="menu-item">
                        <FolderTree size={15} />
                        <span>Quản lý danh mục</span>
                      </Link>
                    )}

                    <Link to="/profile" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.5rem 0.75rem', fontSize: '0.8125rem', borderRadius: '0.375rem' }} className="menu-item">
                      <User size={15} />
                      <span>Hồ sơ tác giả</span>
                    </Link>

                    <button
                      onClick={logout}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.5rem',
                        width: '100%',
                        padding: '0.5rem 0.75rem',
                        fontSize: '0.8125rem',
                        color: '#ef4444',
                        borderRadius: '0.375rem',
                        marginTop: '0.25rem',
                        borderTop: '1px solid var(--border)'
                      }}
                    >
                      <LogOut size={15} />
                      <span>Đăng xuất</span>
                    </button>
                  </div>
                )}
              </div>
            </div>
          ) : (
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <Link to="/login" className="btn btn-outline btn-sm">
                Đăng nhập
              </Link>
              <Link to="/register" className="btn btn-primary btn-sm">
                Đăng ký
              </Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};
