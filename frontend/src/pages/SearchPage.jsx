import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { api } from '../api/client';
import { RecipeCard } from '../components/RecipeCard';
import {
  Search,
  X,
  Sparkles,
  BookOpen,
  ChevronLeft,
  ChevronRight,
  TrendingUp,
} from 'lucide-react';

const POPULAR_SEARCHES = ['Phở', 'Bún chả', 'Cơm tấm', 'Bánh mì', 'Gà nướng', 'Salad', 'Thịt kho'];

export const SearchPage = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  const queryParam = searchParams.get('q') || '';
  const currentPage = parseInt(searchParams.get('page') || '1', 10);

  const [searchTerm, setSearchTerm] = useState(queryParam);
  const [results, setResults] = useState([]);
  const [meta, setMeta] = useState({ page: 1, pageSize: 12, total: 0, totalPages: 1 });
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  useEffect(() => {
    setSearchTerm(queryParam);
    if (!queryParam.trim()) {
      setResults([]);
      setHasSearched(false);
      return;
    }

    const executeSearch = async () => {
      setLoading(true);
      setHasSearched(true);
      try {
        const res = await api.get('/recipes/search', {
          q: queryParam.trim(),
          page: currentPage,
          pageSize: 12,
        });
        setResults(res?.items || []);
        if (res?.meta) {
          setMeta(res.meta);
        }
      } catch (err) {
        console.error('Failed to execute full-text search:', err);
        setResults([]);
      } finally {
        setLoading(false);
      }
    };

    executeSearch();
  }, [queryParam, currentPage]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (searchTerm.trim()) {
      setSearchParams({ q: searchTerm.trim(), page: '1' });
    }
  };

  const handleTagClick = (tag) => {
    setSearchTerm(tag);
    setSearchParams({ q: tag, page: '1' });
  };

  const handlePageChange = (newPage) => {
    setSearchParams({ q: queryParam, page: newPage });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="container" style={{ padding: '3.5rem 1.25rem 5rem' }}>
      
      {/* Header & Search Bar Box */}
      <div style={{ maxWidth: '720px', margin: '0 auto 3rem', textAlign: 'center' }}>
        <h1 style={{ fontSize: '2.25rem', fontWeight: 800, marginBottom: '0.75rem' }}>
          Tìm Kiếm Công Thức
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1rem', marginBottom: '2rem' }}>
          Tìm nhanh theo tên món ăn, nguyên liệu hoặc cách chế biến với Full-Text Search.
        </p>

        <form onSubmit={handleSearchSubmit} style={{ position: 'relative', marginBottom: '1.25rem' }}>
          <input
            type="text"
            className="input"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Nhập món ăn, nguyên liệu (ví dụ: Phở bò, Gà rán, Nấm...)"
            style={{
              paddingLeft: '3rem',
              paddingRight: searchTerm ? '6.5rem' : '4.5rem',
              height: '3.25rem',
              fontSize: '1rem',
              borderRadius: '2rem',
              boxShadow: '0 4px 12px rgba(0,0,0,0.06)',
            }}
          />
          <Search
            size={20}
            style={{
              position: 'absolute',
              left: '1.25rem',
              top: '50%',
              transform: 'translateY(-50%)',
              color: 'var(--text-muted)',
            }}
          />
          {searchTerm && (
            <button
              type="button"
              onClick={() => setSearchTerm('')}
              style={{
                position: 'absolute',
                right: '4.5rem',
                top: '50%',
                transform: 'translateY(-50%)',
                background: 'none',
                border: 'none',
                color: 'var(--text-muted)',
                cursor: 'pointer',
                padding: '0.25rem',
              }}
            >
              <X size={16} />
            </button>
          )}
          <button
            type="submit"
            className="btn btn-primary"
            style={{
              position: 'absolute',
              right: '0.375rem',
              top: '50%',
              transform: 'translateY(-50%)',
              borderRadius: '1.5rem',
              padding: '0.5rem 1rem',
              fontSize: '0.875rem',
            }}
          >
            Tìm
          </button>
        </form>

        {/* Popular Search Suggestions */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', flexWrap: 'wrap', gap: '0.5rem' }}>
          <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', display: 'inline-flex', alignItems: 'center', gap: '0.25rem' }}>
            <TrendingUp size={14} />
            Gợi ý:
          </span>
          {POPULAR_SEARCHES.map((tag) => (
            <button
              key={tag}
              type="button"
              onClick={() => handleTagClick(tag)}
              style={{
                background: '#f1f5f9',
                border: '1px solid #e2e8f0',
                borderRadius: '1rem',
                padding: '0.25rem 0.75rem',
                fontSize: '0.75rem',
                cursor: 'pointer',
                color: 'var(--secondary)',
                fontWeight: 500,
                transition: 'all 0.15s',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.backgroundColor = '#e2e8f0';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.backgroundColor = '#f1f5f9';
              }}
            >
              {tag}
            </button>
          ))}
        </div>
      </div>

      {/* Results Section */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '4rem 0', color: 'var(--text-muted)' }}>
          Đang tìm kiếm công thức...
        </div>
      ) : hasSearched ? (
        <div>
          {/* Results summary bar */}
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem', borderBottom: '1px solid var(--border)', paddingBottom: '1rem' }}>
            <div>
              <span style={{ fontSize: '1.125rem', fontWeight: 600 }}>
                Kết quả tìm kiếm cho: <span style={{ color: 'var(--primary)' }}>"{queryParam}"</span>
              </span>
              <span style={{ color: 'var(--text-muted)', fontSize: '0.875rem', marginLeft: '0.75rem' }}>
                ({meta.total} kết quả)
              </span>
            </div>
          </div>

          {results.length === 0 ? (
            <div
              style={{
                textAlign: 'center',
                padding: '4rem 2rem',
                backgroundColor: '#ffffff',
                borderRadius: '1rem',
                border: '1px solid var(--border)',
                maxWidth: '600px',
                margin: '0 auto',
              }}
            >
              <BookOpen size={48} style={{ color: 'var(--text-muted)', margin: '0 auto 1rem', opacity: 0.4 }} />
              <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem' }}>Không tìm thấy công thức phù hợp</h3>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.875rem', marginBottom: '1.5rem' }}>
                Thử tìm với từ khóa ngắn hơn, không dấu hoặc xem danh sách tất cả các món ăn.
              </p>
              <Link to="/recipes" className="btn btn-outline">
                <span>Xem tất cả công thức</span>
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
                {results.map((recipe) => (
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
        </div>
      ) : null}
    </div>
  );
};
