import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { User, Mail, Shield, Calendar, Edit3, CheckCircle, AlertCircle } from 'lucide-react';

export const ProfilePage = () => {
  const { user, updateProfile } = useAuth();

  const [fullName, setFullName] = useState(user?.fullName || '');
  const [bio, setBio] = useState(user?.bio || '');
  const [avatarUrl, setAvatarUrl] = useState(user?.avatarUrl || '');
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      await updateProfile({
        fullName: fullName.trim(),
        bio: bio.trim(),
        avatarUrl: avatarUrl.trim(),
      });
      setSuccess('Thông tin tài khoản đã được cập nhật thành công!');
    } catch (err) {
      setError(err.message || 'Cập nhật thông tin thất bại');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="container" style={{ padding: '3.5rem 1.25rem 6rem', maxWidth: '760px' }}>
      
      {/* Title */}
      <div style={{ marginBottom: '2.5rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>Hồ Sơ Cá Nhân</h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
          Quản lý thông tin hồ sơ và tác giả ẩm thực của bạn
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

      <div className="card" style={{ padding: '2.5rem' }}>
        
        {/* Avatar & Header */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', marginBottom: '2rem', paddingBottom: '2rem', borderBottom: '1px solid var(--border)' }}>
          <img
            src={avatarUrl || user?.avatarUrl || `https://api.dicebear.com/7.x/avataaars/svg?seed=${user?.email || 'chef'}`}
            alt="Avatar"
            style={{ width: '5rem', height: '5rem', borderRadius: '50%', objectFit: 'cover', border: '3px solid var(--primary-light)' }}
          />
          <div>
            <h2 style={{ fontSize: '1.25rem', marginBottom: '0.25rem' }}>{user?.fullName || 'Chưa đặt tên'}</h2>
            <div style={{ display: 'flex', gap: '0.75rem', alignItems: 'center', flexWrap: 'wrap' }}>
              <span className="badge badge-published" style={{ textTransform: 'uppercase', fontSize: '0.6875rem' }}>
                {user?.role || 'Author'}
              </span>
              <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                <Mail size={13} /> {user?.email}
              </span>
            </div>
          </div>
        </div>

        {/* Update Form */}
        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          <div className="form-group">
            <label className="form-label" style={{ fontWeight: 600 }}>Họ và tên hiển thị</label>
            <input
              type="text"
              className="form-control"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              placeholder="VD: Nguyễn Hoài Nam"
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label" style={{ fontWeight: 600 }}>URL Ảnh đại diện</label>
            <input
              type="url"
              className="form-control"
              value={avatarUrl}
              onChange={(e) => setAvatarUrl(e.target.value)}
              placeholder="https://images.unsplash.com/..."
            />
          </div>

          <div className="form-group">
            <label className="form-label" style={{ fontWeight: 600 }}>Tiểu sử / Giới thiệu tác giả (Bio)</label>
            <textarea
              rows={4}
              className="form-control"
              value={bio}
              onChange={(e) => setBio(e.target.value)}
              placeholder="Chia sẻ niềm đam mê ẩm thực, kinh nghiệm nấu ăn và phong cách món ăn của bạn..."
            />
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '1rem' }}>
            <button
              type="submit"
              className="btn btn-primary"
              disabled={submitting}
              style={{ minWidth: '160px' }}
            >
              {submitting ? 'Đang lưu...' : 'Lưu Thay Đổi'}
            </button>
          </div>
        </form>

      </div>
    </div>
  );
};
