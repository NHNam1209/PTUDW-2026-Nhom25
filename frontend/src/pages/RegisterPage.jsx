import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { Lock, Mail, User, Check, X, ArrowRight } from 'lucide-react';

export const RegisterPage = () => {
  const [fullName, setFullName] = useState('');
  const [userName, setUserName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const { register } = useAuth();
  const navigate = useNavigate();

  // Password rules validation
  const hasMinLen = password.length >= 8;
  const hasUpper = /[A-Z]/.test(password);
  const hasLower = /[a-z]/.test(password);
  const hasDigit = /\d/.test(password);
  const hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  const isPasswordValid = hasMinLen && hasUpper && hasLower && hasDigit && hasSpecial;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isPasswordValid) {
      setError('Mật khẩu chưa đáp ứng đủ các tiêu chuẩn bảo mật.');
      return;
    }

    setError(null);
    setLoading(true);

    try {
      await register(fullName, email, userName, password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Đăng ký không thành công. Vui lòng kiểm tra lại thông tin.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container" style={{ padding: '3.5rem 1.25rem 5rem', maxWidth: '480px' }}>
      <div className="card" style={{ padding: '2.5rem', boxShadow: '0 10px 25px rgba(0,0,0,0.06)' }}>
        
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <h1 style={{ fontSize: '1.75rem', marginBottom: '0.5rem' }}>Đăng Ký Tài Khoản</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem' }}>
            Trở thành Tác giả và tham gia cộng đồng ẩm thực Culinary Blog
          </p>
        </div>

        {error && (
          <div className="alert alert-error">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.125rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.8125rem', fontWeight: 600, marginBottom: '0.375rem', color: 'var(--secondary)' }}>
              Họ và tên
            </label>
            <div style={{ position: 'relative' }}>
              <input
                type="text"
                required
                placeholder="Nguyễn Văn A"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="input"
                style={{ paddingLeft: '2.5rem' }}
              />
              <User size={16} style={{ position: 'absolute', left: '0.875rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            </div>
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.8125rem', fontWeight: 600, marginBottom: '0.375rem', color: 'var(--secondary)' }}>
              Tên người dùng (Username)
            </label>
            <input
              type="text"
              required
              placeholder="nguyenvana"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              className="input"
            />
          </div>

          <div>
            <label style={{ display: 'block', fontSize: '0.8125rem', fontWeight: 600, marginBottom: '0.375rem', color: 'var(--secondary)' }}>
              Email
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
            <label style={{ display: 'block', fontSize: '0.8125rem', fontWeight: 600, marginBottom: '0.375rem', color: 'var(--secondary)' }}>
              Mật khẩu
            </label>
            <div style={{ position: 'relative' }}>
              <input
                type="password"
                required
                placeholder="Tối thiểu 8 ký tự..."
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="input"
                style={{ paddingLeft: '2.5rem' }}
              />
              <Lock size={16} style={{ position: 'absolute', left: '0.875rem', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            </div>

            {/* Password Validation Requirements List */}
            <div style={{ marginTop: '0.75rem', padding: '0.75rem', backgroundColor: 'var(--bg-main)', borderRadius: '0.5rem', fontSize: '0.75rem', display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
              <span style={{ fontWeight: 600, color: 'var(--secondary)', marginBottom: '0.25rem' }}>Yêu cầu mật khẩu:</span>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', color: hasMinLen ? '#059669' : 'var(--text-muted)' }}>
                {hasMinLen ? <Check size={12} /> : <X size={12} />}
                <span>Ít nhất 8 ký tự</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', color: hasUpper ? '#059669' : 'var(--text-muted)' }}>
                {hasUpper ? <Check size={12} /> : <X size={12} />}
                <span>Chứa chữ in hoa (A-Z)</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', color: hasLower ? '#059669' : 'var(--text-muted)' }}>
                {hasLower ? <Check size={12} /> : <X size={12} />}
                <span>Chứa chữ thường (a-z)</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', color: hasDigit ? '#059669' : 'var(--text-muted)' }}>
                {hasDigit ? <Check size={12} /> : <X size={12} />}
                <span>Chứa chữ số (0-9)</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', color: hasSpecial ? '#059669' : 'var(--text-muted)' }}>
                {hasSpecial ? <Check size={12} /> : <X size={12} />}
                <span>Chứa ký tự đặc biệt (!@#$...)</span>
              </div>
            </div>
          </div>

          <button
            type="submit"
            className="btn btn-primary"
            disabled={loading || !isPasswordValid}
            style={{ width: '100%', marginTop: '0.75rem', opacity: loading || !isPasswordValid ? 0.7 : 1 }}
          >
            <span>{loading ? 'Đang khởi tạo tài khoản...' : 'Đăng ký tài khoản'}</span>
            <ArrowRight size={16} />
          </button>
        </form>

        <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', textAlign: 'center', marginTop: '1.75rem' }}>
          Đã có tài khoản?{' '}
          <Link to="/login" style={{ color: 'var(--primary)', fontWeight: 700 }}>
            Đăng nhập
          </Link>
        </p>

      </div>
    </div>
  );
};
