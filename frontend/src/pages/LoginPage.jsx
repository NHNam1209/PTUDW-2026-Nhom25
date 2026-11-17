import React, { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Lock, Mail, ArrowRight, ShieldCheck } from 'lucide-react';

export const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [googleLoading, setGoogleLoading] = useState(false);

  const { login, loginWithGoogle } = useAuth();
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

  const handleGoogleLogin = async () => {
    setError(null);
    setGoogleLoading(true);

    try {
      // Create dev mock JWT token with Google identity payload for smooth demonstration & testing
      const header = btoa(JSON.stringify({ alg: "HS256", typ: "JWT" }));
      const payload = btoa(
        JSON.stringify({
          iss: "https://accounts.google.com",
          sub: "google-oauth2-108273918237192",
          email: "google.user@culinaryblog.com",
          email_verified: true,
          name: "Nguyễn Google User",
          picture: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150",
          exp: Math.floor(Date.now() / 1000) + 3600,
        })
      );
      const mockIdToken = `${header}.${payload}.devsignature`;

      await loginWithGoogle(mockIdToken);
      navigate(from, { replace: true });
    } catch (err) {
      setError(err.message || 'Đăng nhập bằng Google không thành công.');
    } finally {
      setGoogleLoading(false);
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
            disabled={loading || googleLoading}
            style={{ width: '100%', marginTop: '0.5rem', opacity: loading ? 0.7 : 1 }}
          >
            <span>{loading ? 'Đang xác thực...' : 'Đăng nhập'}</span>
            <ArrowRight size={16} />
          </button>
        </form>

        {/* FR-AUTH-UI-001: Google OAuth 2.0 Sign In Button */}
        <div style={{ display: 'flex', alignItems: 'center', margin: '1.5rem 0' }}>
          <div style={{ flex: 1, height: '1px', backgroundColor: 'var(--border)' }} />
          <span style={{ padding: '0 0.75rem', fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase' }}>
            hoặc tiếp tục với
          </span>
          <div style={{ flex: 1, height: '1px', backgroundColor: 'var(--border)' }} />
        </div>

        <button
          type="button"
          onClick={handleGoogleLogin}
          disabled={loading || googleLoading}
          className="btn btn-outline"
          style={{
            width: '100%',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '0.75rem',
            padding: '0.75rem',
            backgroundColor: '#ffffff',
            border: '1px solid #e2e8f0',
            fontWeight: 600,
            fontSize: '0.875rem',
            borderRadius: '0.5rem',
            transition: 'all 0.2s',
          }}
        >
          <svg width="18" height="18" viewBox="0 0 24 24">
            <path
              fill="#4285F4"
              d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
            />
            <path
              fill="#34A853"
              d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
            />
            <path
              fill="#FBBC05"
              d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"
            />
            <path
              fill="#EA4335"
              d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"
            />
          </svg>
          <span>{googleLoading ? 'Đang kết nối Google...' : 'Đăng nhập bằng Google'}</span>
        </button>

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
