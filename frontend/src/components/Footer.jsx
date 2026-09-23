import React from 'react';
import { Link } from 'react-router-dom';
import { UtensilsCrossed, Heart } from 'lucide-react';

export const Footer = () => {
  return (
    <footer style={{ backgroundColor: '#ffffff', borderTop: '1px solid var(--border)', marginTop: '4rem', padding: '3.5rem 0 2rem' }}>
      <div className="container">
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '2.5rem', marginBottom: '2.5rem' }}>
          
          {/* Brand Col */}
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.625rem', marginBottom: '1rem' }}>
              <div style={{
                width: '2.25rem',
                height: '2.25rem',
                backgroundColor: 'var(--primary)',
                borderRadius: '0.625rem',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#ffffff'
              }}>
                <UtensilsCrossed size={18} />
              </div>
              <span style={{ fontSize: '1.25rem', fontWeight: 800, color: 'var(--secondary)' }}>
                Culinary<span style={{ color: 'var(--primary)' }}>Blog</span>
              </span>
            </div>
            <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
              Nền tảng blog ẩm thực chia sẻ bí quyết nấu ăn ngon, phong phú từ các đầu bếp gia đình và chuyên nghiệp trên khắp mọi miền Việt Nam.
            </p>
          </div>

          {/* Quick links */}
          <div>
            <h4 style={{ fontSize: '0.875rem', fontWeight: 700, color: 'var(--secondary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '1rem' }}>
              Khám phá
            </h4>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.625rem', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
              <li><Link to="/recipes">Tất cả công thức</Link></li>
              <li><Link to="/categories/mon-khai-vi">Món khai vị</Link></li>
              <li><Link to="/categories/mon-chinh">Món chính</Link></li>
              <li><Link to="/categories/mon-trang-mieng">Món tráng miệng</Link></li>
              <li><Link to="/categories/mon-chay">Món chay dinh dưỡng</Link></li>
            </ul>
          </div>

          {/* Development Team */}
          <div>
            <h4 style={{ fontSize: '0.875rem', fontWeight: 700, color: 'var(--secondary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '1rem' }}>
              Nhóm Phát Triển (Nhóm 25)
            </h4>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.5rem', fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
              <li><strong>Nguyễn Hoài Nam (Lead)</strong> - 2312607</li>
              <li><strong>Đỗ Duy Biên</strong> - 2312584</li>
              <li><strong>Hoàng Thăng Long</strong> - 2312676</li>
              <li><strong>Trần Chánh Phát</strong> - 2212437</li>
            </ul>
          </div>

          {/* Technology */}
          <div>
            <h4 style={{ fontSize: '0.875rem', fontWeight: 700, color: 'var(--secondary)', textTransform: 'uppercase', letterSpacing: '0.05em', marginBottom: '1rem' }}>
              Công nghệ ứng dụng
            </h4>
            <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
              Xây dựng với Python FastAPI, PostgreSQL, Docker, React, MinIO S3 và Redis Cache theo chuẩn đặc tả phần mềm SRS v1.0.0.
            </p>
          </div>
        </div>

        {/* Bottom copyright */}
        <div style={{
          borderTop: '1px solid var(--border)',
          paddingTop: '1.5rem',
          display: 'flex',
          flexWrap: 'wrap',
          alignItems: 'center',
          justifyContent: 'space-between',
          fontSize: '0.8125rem',
          color: 'var(--text-muted)',
          gap: '1rem'
        }}>
          <div>© 2026 Culinary Blog - Phát triển Ứng dụng Web Nâng cao. All rights reserved.</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
            <span>Thực hiện với</span>
            <Heart size={14} color="#ef4444" fill="#ef4444" />
            <span>bởi Nhóm 25</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
