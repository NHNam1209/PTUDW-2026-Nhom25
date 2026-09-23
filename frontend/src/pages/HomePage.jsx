import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { RecipeCard } from '../components/RecipeCard';
import { Search, Sparkles, BookOpen, ChefHat, ArrowRight } from 'lucide-react';

export const HomePage = () => {
  const [categories, setCategories] = useState([]);
  const [featuredRecipes, setFeaturedRecipes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [catData, rcpData] = await Promise.all([
          api.get('/categories'),
          api.get('/recipes', { pageSize: 6, sort: '-createdAt' }),
        ]);
        setCategories(catData || []);
        setFeaturedRecipes(rcpData?.items || []);
      } catch (err) {
        console.error('Error fetching homepage data:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/recipes?q=${encodeURIComponent(searchQuery.trim())}`);
    }
  };

  return (
    <div>
      {/* Hero Banner Section */}
      <section style={{
        background: 'linear-gradient(135deg, #fff7ed 0%, #ffedd5 50%, #fed7aa 100%)',
        padding: '5rem 0 4.5rem',
        borderBottom: '1px solid var(--border)',
        position: 'relative',
        overflow: 'hidden'
      }}>
        <div className="container" style={{ textAlign: 'center', maxWidth: '800px' }}>
          
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', backgroundColor: '#ffffff', padding: '0.375rem 1rem', borderRadius: '9999px', fontSize: '0.8125rem', fontWeight: 600, color: 'var(--primary)', marginBottom: '1.5rem', boxShadow: '0 2px 8px rgba(249, 115, 22, 0.15)' }}>
            <Sparkles size={16} />
            <span>Nền tảng Ẩm thực Trực tuyến Hàng đầu</span>
          </div>

          <h1 style={{ fontSize: '3rem', lineHeight: 1.15, marginBottom: '1.25rem', color: 'var(--secondary)' }}>
            Khám Phá & Sáng Tạo <br />
            <span style={{ color: 'var(--primary)', fontStyle: 'italic' }}>Món Ngon Mỗi Ngày</span>
          </h1>

          <p style={{ fontSize: '1.125rem', color: 'var(--text-muted)', marginBottom: '2.5rem', lineHeight: 1.6 }}>
            Hàng trăm công thức nấu ăn chuẩn vị truyền thống và hiện đại, hướng dẫn chi tiết từng bước, định lượng dinh dưỡng chuẩn xác.
          </p>

          {/* Search Box in Hero */}
          <form onSubmit={handleSearchSubmit} style={{ display: 'flex', gap: '0.5rem', maxWidth: '36rem', margin: '0 auto', backgroundColor: '#ffffff', padding: '0.375rem', borderRadius: '9999px', boxShadow: '0 10px 25px rgba(0, 0, 0, 0.08)', border: '1px solid var(--border)' }}>
            <div style={{ display: 'flex', alignItems: 'center', flex: 1, paddingLeft: '1rem' }}>
              <Search size={18} color="var(--text-muted)" />
              <input
                type="text"
                placeholder="Bạn muốn nấu món gì hôm nay? (Phở, nem, súp...)"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                style={{ width: '100%', border: 'none', outline: 'none', padding: '0.625rem 0.75rem', fontSize: '0.9375rem', color: 'var(--secondary)' }}
              />
            </div>
            <button type="submit" className="btn btn-primary" style={{ padding: '0.625rem 1.5rem' }}>
              Tìm kiếm
            </button>
          </form>

        </div>
      </section>

      {/* Categories Section */}
      <section style={{ padding: '4rem 0' }}>
        <div className="container">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '2rem' }}>
            <div>
              <span style={{ fontSize: '0.8125rem', fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Phân loại ẩm thực
              </span>
              <h2 style={{ fontSize: '1.75rem', marginTop: '0.25rem' }}>Danh Mục Món Ăn</h2>
            </div>
            <Link to="/recipes" style={{ display: 'flex', alignItems: 'center', gap: '0.375rem', fontSize: '0.875rem', fontWeight: 600, color: 'var(--primary)' }}>
              <span>Xem tất cả</span>
              <ArrowRight size={16} />
            </Link>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '1.25rem' }}>
            {categories.map((cat) => (
              <Link
                key={cat.id}
                to={`/recipes?categoryId=${cat.id}`}
                className="card"
                style={{
                  padding: '1.5rem 1.25rem',
                  textAlign: 'center',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  textDecoration: 'none',
                }}
              >
                <div style={{
                  width: '3.5rem',
                  height: '3.5rem',
                  borderRadius: '1rem',
                  backgroundColor: 'var(--primary-light)',
                  color: 'var(--primary)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginBottom: '1rem'
                }}>
                  <ChefHat size={28} />
                </div>
                <h4 style={{ fontSize: '1rem', fontWeight: 700, color: 'var(--secondary)', marginBottom: '0.25rem' }}>
                  {cat.name}
                </h4>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                  {cat.recipeCount} công thức
                </span>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Recipes Section */}
      <section style={{ padding: '2rem 0 4rem', backgroundColor: '#ffffff', borderTop: '1px solid var(--border)', borderBottom: '1px solid var(--border)' }}>
        <div className="container">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '2.5rem' }}>
            <div>
              <span style={{ fontSize: '0.8125rem', fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Mới cập nhật
              </span>
              <h2 style={{ fontSize: '1.75rem', marginTop: '0.25rem' }}>Công Thức Mới Nhất</h2>
            </div>
            <Link to="/recipes" className="btn btn-outline btn-sm">
              <span>Khám phá kho công thức</span>
              <ArrowRight size={14} />
            </Link>
          </div>

          {loading ? (
            <div style={{ textAlign: 'center', padding: '3rem', color: 'var(--text-muted)' }}>
              Đang tải dữ liệu công thức...
            </div>
          ) : featuredRecipes.length > 0 ? (
            <div className="grid grid-cols-3">
              {featuredRecipes.map((recipe) => (
                <RecipeCard key={recipe.id} recipe={recipe} />
              ))}
            </div>
          ) : (
            <div style={{ textAlign: 'center', padding: '3rem', backgroundColor: 'var(--bg-main)', borderRadius: '1rem' }}>
              <p style={{ color: 'var(--text-muted)', marginBottom: '1rem' }}>Chưa có công thức nào được xuất bản.</p>
              <Link to="/dashboard/recipes/new" className="btn btn-primary btn-sm">
                Đăng công thức đầu tiên
              </Link>
            </div>
          )}
        </div>
      </section>

      {/* Culinary Community Features */}
      <section style={{ padding: '5rem 0' }}>
        <div className="container">
          <div style={{ textAlign: 'center', maxWidth: '600px', margin: '0 auto 3rem' }}>
            <span style={{ fontSize: '0.8125rem', fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Nền tảng tiện ích
            </span>
            <h2 style={{ fontSize: '2rem', marginTop: '0.25rem', marginBottom: '0.75rem' }}>
              Mọi Thứ Bạn Cần Để Nấu Ăn Thành Công
            </h2>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.9375rem' }}>
              Trải nghiệm nấu nướng chuẩn hóa với các công cụ hỗ trợ người nấu từ chuẩn bị nguyên liệu đến canh thời gian.
            </p>
          </div>

          <div className="grid grid-cols-3">
            <div className="card" style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{ width: '3rem', height: '3rem', backgroundColor: '#ecfdf5', color: '#059669', borderRadius: '0.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1.25rem' }}>
                <BookOpen size={24} />
              </div>
              <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>Hướng Dẫn Từng Bước</h3>
              <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
                Các bước thực hiện được phân chia rõ ràng kèm hình ảnh minh họa và bộ đếm thời gian cho từng công đoạn.
              </p>
            </div>

            <div className="card" style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{ width: '3rem', height: '3rem', backgroundColor: '#fffbeb', color: '#d97706', borderRadius: '0.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1.25rem' }}>
                <Sparkles size={24} />
              </div>
              <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>Định Lượng Dinh Dưỡng</h3>
              <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
                Theo dõi chi tiết Calories, Protein, Carbs, Chất béo, Chất xơ giúp bạn duy trì lối sống lành mạnh khoa học.
              </p>
            </div>

            <div className="card" style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{ width: '3rem', height: '3rem', backgroundColor: '#eff6ff', color: '#2563eb', borderRadius: '0.75rem', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1.25rem' }}>
                <ChefHat size={24} />
              </div>
              <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>Cộng Đồng Đam Mê</h3>
              <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', lineHeight: 1.6 }}>
                Dễ dàng trở thành Tác giả, chia sẻ những công thức bí truyền của gia đình bạn với hàng nghìn độc giả.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
