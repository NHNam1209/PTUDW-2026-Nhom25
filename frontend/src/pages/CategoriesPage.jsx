import React, { useState, useEffect } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import { api } from '../api/client';
import { RecipeCard } from '../components/RecipeCard';
import {
  FolderTree,
  BookOpen,
  ChevronRight,
  ArrowLeft,
  ChevronLeft,
  Sparkles,
} from 'lucide-react';

export const CategoriesPage = () => {
  const { slug } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const currentPage = parseInt(searchParams.get('page') || '1', 10);

  const [categories, setCategories] = useState([]);
  const [activeCategory, setActiveCategory] = useState(null);
  const [categoryRecipes, setCategoryRecipes] = useState([]);
  const [meta, setMeta] = useState({ page: 1, pageSize: 12, total: 0, totalPages: 1 });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch all categories for listing or sidebar
  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const data = await api.get('/categories');
        setCategories(data || []);
      } catch (err) {
        console.error('Failed to load categories:', err);
      }
    };
    fetchCategories();
  }, []);

  // If a slug is present, fetch category detail and its recipes
  useEffect(() => {
    if (!slug) {
      setActiveCategory(null);
      setCategoryRecipes([]);
      setLoading(false);
      return;
    }

    const fetchCategoryDetail = async () => {
      setLoading(true);
      setError(null);
      try {
        const res = await api.get(`/categories/${slug}`, {
          page: currentPage,
          pageSize: 12,
        });
        setActiveCategory(res?.category || null);
        setCategoryRecipes(res?.recipes?.items || []);
        if (res?.recipes?.meta) {
          setMeta(res.recipes.meta);
        }
      } catch (err) {
        console.error('Failed to load category details:', err);
        setError('Không tìm thấy danh mục hoặc danh mục chưa có công thức nấu ăn.');
      } finally {
        setLoading(false);
      }
    };

    fetchCategoryDetail();
  }, [slug, currentPage]);

  const handlePageChange = (newPage) => {
    setSearchParams({ page: newPage });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // 1. DETAIL VIEW: Category Recipes Listing
  if (slug) {
    return (
      <div className="container" style={{ padding: '2.5rem 1.25rem 5rem' }}>
        {/* Breadcrumb Navigation */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.875rem', color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
          <Link to="/" style={{ color: 'var(--text-muted)', textDecoration: 'none' }}>Trang chủ</Link>
          <ChevronRight size={14} />
          <Link to="/categories" style={{ color: 'var(--text-muted)', textDecoration: 'none' }}>Danh mục</Link>
          <ChevronRight size={14} />
          <span style={{ color: 'var(--primary)', fontWeight: 600 }}>{activeCategory?.name || slug}</span>
        </div>

        <Link
          to="/categories"
          className="btn btn-outline btn-sm"
          style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', marginBottom: '2rem' }}
        >
          <ArrowLeft size={16} />
          <span>Tất cả danh mục</span>
        </Link>

        {loading ? (
          <div style={{ textAlign: 'center', padding: '5rem 0', color: 'var(--text-muted)' }}>
            Đang tải dữ liệu danh mục...
          </div>
        ) : error ? (
          <div className="alert alert-error" style={{ margin: '2rem 0' }}>
            {error}
          </div>
        ) : (
          <>
            {/* Category Header Banner */}
            <div
              style={{
                backgroundColor: '#ffffff',
                borderRadius: '1rem',
                border: '1px solid var(--border)',
                padding: '2rem',
                marginBottom: '2.5rem',
                display: 'flex',
                flexDirection: 'column',
                gap: '1rem',
                boxShadow: '0 2px 4px rgba(0,0,0,0.03)',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                <div
                  style={{
                    width: '56px',
                    height: '56px',
                    borderRadius: '0.75rem',
                    backgroundColor: '#fff7ed',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    color: 'var(--primary)',
                  }}
                >
                  <FolderTree size={28} />
                </div>
                <div>
                  <h1 style={{ fontSize: '2rem', margin: 0, fontWeight: 700 }}>{activeCategory?.name}</h1>
                  <p style={{ color: 'var(--text-muted)', margin: '0.25rem 0 0', fontSize: '0.9375rem' }}>
                    {activeCategory?.description || 'Khám phá các công thức đặc sắc trong danh mục này.'}
                  </p>
                </div>
              </div>
              <div style={{ fontSize: '0.875rem', color: 'var(--text-muted)' }}>
                Tổng cộng: <strong style={{ color: 'var(--secondary)' }}>{meta.total}</strong> món ăn
              </div>
            </div>

            {/* Recipes Grid */}
            {categoryRecipes.length === 0 ? (
              <div
                style={{
                  textAlign: 'center',
                  padding: '4rem 2rem',
                  backgroundColor: '#ffffff',
                  borderRadius: '1rem',
                  border: '1px solid var(--border)',
                }}
              >
                <BookOpen size={48} style={{ color: 'var(--text-muted)', margin: '0 auto 1rem', opacity: 0.5 }} />
                <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>Chưa có công thức trong danh mục này</h3>
                <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem', marginBottom: '1.5rem' }}>
                  Hãy là người đầu tiên chia sẻ công thức món ăn tuyệt vời này!
                </p>
                <Link to="/dashboard/recipes/new" className="btn btn-primary">
                  <span>Tạo công thức mới</span>
                </Link>
              </div>
            ) : (
              <>
                <div
                  style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
                    gap: '1.75rem',
                  }}
                >
                  {categoryRecipes.map((recipe) => (
                    <RecipeCard key={recipe.id} recipe={recipe} />
                  ))}
                </div>

                {/* Pagination */}
                {meta.totalPages > 1 && (
                  <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5rem', marginTop: '3.5rem' }}>
                    <button
                      onClick={() => handlePageChange(meta.page - 1)}
                      disabled={meta.page <= 1}
                      className="btn btn-outline btn-sm"
                    >
                      <ChevronLeft size={16} />
                      <span>Trước</span>
                    </button>
                    <span style={{ fontSize: '0.875rem', padding: '0 0.75rem', color: 'var(--text-muted)' }}>
                      Trang {meta.page} / {meta.totalPages}
                    </span>
                    <button
                      onClick={() => handlePageChange(meta.page + 1)}
                      disabled={meta.page >= meta.totalPages}
                      className="btn btn-outline btn-sm"
                    >
                      <span>Sau</span>
                      <ChevronRight size={16} />
                    </button>
                  </div>
                )}
              </>
            )}
          </>
        )}
      </div>
    );
  }

  // 2. OVERVIEW: All Categories Grid
  return (
    <div className="container" style={{ padding: '3rem 1.25rem 5rem' }}>
      <div style={{ marginBottom: '2.5rem', textAlign: 'center' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.375rem 0.875rem', backgroundColor: '#fff7ed', color: 'var(--primary)', borderRadius: '2rem', fontSize: '0.8125rem', fontWeight: 600, marginBottom: '0.75rem' }}>
          <Sparkles size={14} />
          <span>Khám phá ẩm thực theo chủ đề</span>
        </div>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 800, marginBottom: '0.5rem' }}>Danh Mục Món Ăn</h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1rem', maxWidth: '600px', margin: '0 auto' }}>
          Tuyển tập các danh mục ẩm thực phong phú từ món khai vị, món chính đến tráng miệng và đồ uống.
        </p>
      </div>

      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
          gap: '1.75rem',
        }}
      >
        {categories.map((cat) => (
          <Link
            key={cat.id}
            to={`/categories/${cat.slug}`}
            style={{ textDecoration: 'none', color: 'inherit' }}
          >
            <div
              className="card"
              style={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                borderRadius: '1rem',
                overflow: 'hidden',
                transition: 'transform 0.2s, box-shadow 0.2s',
                border: '1px solid var(--border)',
                cursor: 'pointer',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-4px)';
                e.currentTarget.style.boxShadow = '0 12px 24px rgba(0,0,0,0.08)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = 'none';
              }}
            >
              <div
                style={{
                  height: '160px',
                  backgroundColor: '#f8fafc',
                  backgroundImage: cat.imageUrl ? `url(${cat.imageUrl})` : undefined,
                  backgroundSize: 'cover',
                  backgroundPosition: 'center',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  position: 'relative',
                }}
              >
                {!cat.imageUrl && (
                  <FolderTree size={48} style={{ color: 'var(--text-muted)', opacity: 0.4 }} />
                )}
                <div
                  style={{
                    position: 'absolute',
                    top: '0.75rem',
                    right: '0.75rem',
                    backgroundColor: 'rgba(0,0,0,0.65)',
                    backdropFilter: 'blur(4px)',
                    color: '#ffffff',
                    padding: '0.25rem 0.625rem',
                    borderRadius: '1rem',
                    fontSize: '0.75rem',
                    fontWeight: 600,
                  }}
                >
                  {cat.recipeCount || 0} công thức
                </div>
              </div>

              <div style={{ padding: '1.5rem', flex: 1, display: 'flex', flexDirection: 'column' }}>
                <h3 style={{ fontSize: '1.25rem', fontWeight: 700, marginBottom: '0.5rem', color: 'var(--secondary)' }}>
                  {cat.name}
                </h3>
                <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', margin: 0, flex: 1, lineHeight: 1.5 }}>
                  {cat.description || 'Các món ngon tuyển chọn dễ nấu tại nhà.'}
                </p>

                <div
                  style={{
                    marginTop: '1.25rem',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.25rem',
                    color: 'var(--primary)',
                    fontWeight: 600,
                    fontSize: '0.8125rem',
                  }}
                >
                  <span>Xem các món ăn</span>
                  <ChevronRight size={16} />
                </div>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};
