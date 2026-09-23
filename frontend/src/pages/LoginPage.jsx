import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Lock, Mail, ArrowRight, ShieldCheck } from 'lucide-react';

export const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const from = location.state?.from?.pathname || '/dashboard';

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      await login(email, password);
      navigate(from, { replace: true });
    } catch (err) {
      setError(err.message || 'Đăng nhập không thành công. Vui lòng kiểm tra lại tài khoản.');
    } finally {
      setLoading(false);
    }
  };

  const fillDemo = (demoEmail, demoPw) => {
    setEmail(demoEmail);
    setPassword(demoPw);
  };

  return (
    <div className="container" style={{ padding: '4rem 1.25rem 6rem', maxWidth: '440px' }}>
      <div className="card" style={{ padding: '2.5rem', boxShadow: '0 10px 25px rgba(0,0,0,0.06)' }}>
        
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h1 style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>Chào Mừng Trở Lại</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
            Đăng nhập để quản lý và chia sẻ công thức nấu ăn của bạn
          </p>
        </div>

        {error && (
          <div className="alert alert-error">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8125rem', fontWeight: 600, marginBottom: '0.375rem', color: 'var(--secondary)' }}>
              Email đăng nhập
            </label>
            <div style={{ position: 'relative' }}>
              <input
                type="email"
                required
                placeholder="name@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="input"
                style={{ paddingLeft: '2.5rem' }}
              />
              <Mail size={16} style={{ position: 'absolute', left: '0.875rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            </div>
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.375rem' }}>
              <label style={{ fontSize: '0.8125rem', fontWeight: 600, color: 'var(--secondary)' }}>
                Mật khẩu
              </label>
            </div>
            <div style={{ position: 'relative' }}>
              <input
                type="password"
                required
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input"
                style={{ paddingLeft: '2.5rem' }}
              />
              <Lock size={16} style={{ position: 'absolute', left: '0.875rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            </div>
          </div>

          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading}
            style={{ width: '100%', marginTop: '0.5rem', opacity: loading ? 0.7 : 1 }}
          >
            <span>{loading ? 'Đang xác thực...' : 'Đăng nhập'}</span>
            <ArrowRight size={16} />
          </button>
        </form>

        {/* Quick Demo Fill Buttons */}
        <div style={{ marginTop: '2rem', paddingTop: '1.5rem', borderTop: '1px solid var(--border)' }}>
          <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '0.75rem', textAlign: 'center', fontWeight: 600 }}>
            Tài khoản dùng thử có sẵn:
          </p>
          <div style={{ display: 'flex', gap: '0.5rem' }}>
            <button
              type="button"
              onClick={() => fillDemo('admin@culinaryblog.com', 'Admin@123456')}
              className="btn btn-outline btn-sm"
              style={{ flex: 1, fontSize: '0.6875rem' }}
            >
              <ShieldCheck size={12} />
              <span>Admin</span>
            </button>
            <button
              type="button"
              onClick={() => fillDemo('namnh.tandt@gmail.com', 'Nam@123456')}
              className="btn btn-outline btn-sm"
              style={{ flex: 1, fontSize: '0.6875rem' }}
            >
              <span>Author (Nam)</span>
            </button>
          </div>
        </div>

        <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', textAlign: 'center', marginTop: '1.75rem' }}>
          Chưa có tài khoản?{' '}
          <Link to="/register" style={{ color: 'var(--primary)', fontWeight: 700 }}>
            Đăng ký ngay
          </Link>
        </p>

      </div>
    </div>
  );
};
