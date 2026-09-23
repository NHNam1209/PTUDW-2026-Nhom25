import React, { useState, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { api } from '../api/client';
import { RecipeCard } from '../components/RecipeCard';
import { Search, Filter, SlidersHorizontal, ChevronLeft, ChevronRight, X } from 'lucide-react';

export const RecipeListPage = () => {
  const [searchParams, setSearchParams] = useSearchParams();
  
  const [recipes, setRecipes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [meta, setMeta] = useState({ page: 1, pageSize: 12, total: 0, totalPages: 1 });
  const [loading, setLoading] = useState(true);

  // Filters state from query params
  const currentCategory = searchParams.get('categoryId') || '';
  const currentDifficulty = searchParams.get('difficulty') || '';
  const currentMaxCookTime = searchParams.get('maxCookTime') || '';
  const currentSort = searchParams.get('sort') || '-createdAt';
  const currentSearch = searchParams.get('q') || '';
  const currentPage = parseInt(searchParams.get('page') || '1', 10);

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

  useEffect(() => {
    const fetchRecipes = async () => {
      setLoading(true);
      try {
        const res = await api.get('/recipes', {
          page: currentPage,
          pageSize: 12,
          categoryId: currentCategory || undefined,
          difficulty: currentDifficulty ? parseInt(currentDifficulty, 10) : undefined,
          maxCookTime: currentMaxCookTime ? parseInt(currentMaxCookTime, 10) : undefined,
          sort: currentSort,
        });
        setRecipes(res?.items || []);
        if (res?.meta) {
          setMeta(res.meta);
        }
      } catch (err) {
        console.error('Failed to fetch recipes:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchRecipes();
  }, [currentCategory, currentDifficulty, currentMaxCookTime, currentSort, currentPage]);

  const updateFilters = (newParams) => {
    const updated = new URLSearchParams(searchParams);
    Object.entries(newParams).forEach(([k, v]) => {
      if (v === '' || v === null || v === undefined) {
        updated.delete(k);
      } else {
        updated.set(k, v);
      }
    });
    // Reset to page 1 on filter change if not paging
    if (!newParams.page) {
      updated.set('page', '1');
    }
    setSearchParams(updated);
  };

  const handlePageChange = (newPage) => {
    updateFilters({ page: newPage });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="container" style={{ padding: '3rem 1.25rem 5rem' }}>
      
      {/* Page Header */}
      <div style={{ marginBottom: '2.5rem' }}>
        <h1 style={{ fontSize: '2.25rem', marginBottom: '0.5rem' }}>Kho Tàng Công Thức Nấu Ăn</h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1rem' }}>
          Tìm kiếm và lọc các món ăn ngon phù hợp với nguyên liệu và thời gian của bạn.
        </p>
      </div>

      {/* Filter and Control Bar */}
      <div style={{
        backgroundColor: '#ffffff',
        borderRadius: '1rem',
        padding: '1.25rem',
        border: '1px solid var(--border)',
        marginBottom: '2.5rem',
        boxShadow: '0 1px 3px rgba(0,0,0,0.04)'
      }}>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem', alignItems: 'center' }}>
          
          {/* Category Select */}
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: '0.375rem' }}>
              Danh mục
            </label>
            <select
              className="select"
              value={currentCategory}
              onChange={(e) => updateFilters({ categoryId: e.target.value })}
            >
              <option value="">Tất cả danh mục</option>
              {categories.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.name}
                </option>
              ))}
            </select>
          </div>

          {/* Difficulty Select */}
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: '0.375rem' }}>
              Độ khó
            </label>
            <select
              className="select"
              value={currentDifficulty}
              onChange={(e) => updateFilters({ difficulty: e.target.value })}
            >
              <option value="">Mọi độ khó</option>
              <option value="1">Dễ</option>
              <option value="2">Vừa</option>
              <option value="3">Khó</option>
              <option value="4">Bếp trưởng</option>
            </select>
          </div>

          {/* Max Cook Time */}
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: '0.375rem' }}>
              Thời gian nấu tối đa
            </label>
            <select
              className="select"
              value={currentMaxCookTime}
              onChange={(e) => updateFilters({ maxCookTime: e.target.value })}
            >
              <option value="">Không giới hạn</option>
              <option value="15">Dưới 15 phút</option>
              <option value="30">Dưới 30 phút</option>
              <option value="60">Dưới 1 tiếng</option>
              <option value="120">Dưới 2 tiếng</option>
            </select>
          </div>

          {/* Sorting */}
          <div>
            <label style={{ display: 'block', fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: '0.375rem' }}>
              Sắp xếp
            </label>
            <select
              className="select"
              value={currentSort}
              onChange={(e) => updateFilters({ sort: e.target.value })}
            >
              <option value="-createdAt">Mới nhất trước</option>
              <option value="createdAt">Cũ nhất trước</option>
              <option value="title">Tên món ăn (A-Z)</option>
              <option value="-title">Tên món ăn (Z-A)</option>
              <option value="cookTime">Thời gian nấu nhanh nhất</option>
            </select>
          </div>

        </div>

        {/* Active Filters Clear */}
        {(currentCategory || currentDifficulty || currentMaxCookTime || currentSearch) && (
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', marginTop: '1rem', paddingTop: '1rem', borderTop: '1px solid var(--border)' }}>
            <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>Đang lọc theo:</span>
            <button
              onClick={() => setSearchParams({})}
              style={{ display: 'flex', alignItems: 'center', gap: '0.25rem', fontSize: '0.75rem', color: 'var(--primary)', fontWeight: 600 }}
            >
              <X size={14} />
              <span>Xóa tất cả bộ lọc</span>
            </button>
          </div>
        )}
      </div>

      {/* Recipes Grid */}
      {loading ? (
        <div style={{ textAlign: 'center', padding: '5rem 0', color: 'var(--text-muted)' }}>
          Đang tải danh sách công thức...
        </div>
      ) : recipes.length > 0 ? (
        <>
          <div className="grid grid-cols-3" style={{ marginBottom: '3rem' }}>
            {recipes.map((recipe) => (
              <RecipeCard key={recipe.id} recipe={recipe} />
            ))}
          </div>

          {/* Pagination Controls */}
          {meta.totalPages > 1 && (
            <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '0.5rem' }}>
              <button
                className="btn btn-outline btn-sm"
                disabled={!meta.hasPreviousPage}
                onClick={() => handlePageChange(meta.page - 1)}
                style={{ opacity: meta.hasPreviousPage ? 1 : 0.5, cursor: meta.hasPreviousPage ? 'pointer' : 'not-allowed' }}
              >
                <ChevronLeft size={16} />
                <span>Trang trước</span>
              </button>

              <span style={{ fontSize: '0.875rem', fontWeight: 600, padding: '0 0.75rem', color: 'var(--secondary)' }}>
                Trang {meta.page} / {meta.totalPages}
              </span>

              <button
                className="btn btn-outline btn-sm"
                disabled={!meta.hasNextPage}
                onClick={() => handlePageChange(meta.page + 1)}
                style={{ opacity: meta.hasNextPage ? 1 : 0.5, cursor: meta.hasNextPage ? 'pointer' : 'not-allowed' }}
              >
                <span>Trang sau</span>
                <ChevronRight size={16} />
              </button>
            </div>
          )}
        </>
      ) : (
        <div style={{ textAlign: 'center', padding: '4rem 1rem', backgroundColor: '#ffffff', borderRadius: '1rem', border: '1px solid var(--border)' }}>
          <p style={{ fontSize: '1.125rem', color: 'var(--secondary)', fontWeight: 600, marginBottom: '0.5rem' }}>
            Không tìm thấy công thức nào phù hợp
          </p>
          <p style={{ fontSize: '0.875rem', color: 'var(--text-muted)', marginBottom: '1.5rem' }}>
            Hãy thử thay đổi điều kiện lọc hoặc từ khóa tìm kiếm.
          </p>
          <button onClick={() => setSearchParams({})} className="btn btn-primary btn-sm">
            Xem tất cả công thức
          </button>
        </div>
      )}

    </div>
  );
};
