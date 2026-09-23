import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { api } from '../api/client';
import { useAuth } from '../context/AuthContext';
import {
  Clock,
  Users,
  Flame,
  CheckCircle2,
  Circle,
  Play,
  Pause,
  RotateCcw,
  Edit,
  ArrowLeft,
  Calendar,
  Share2,
} from 'lucide-react';

const difficultyMap = {
  1: { label: 'Dễ', class: 'badge-easy' },
  2: { label: 'Vừa', class: 'badge-medium' },
  3: { label: 'Khó', class: 'badge-hard' },
  4: { label: 'Bếp trưởng', class: 'badge-expert' },
};

// Cooking Timer Component for Steps
const CookingTimer = ({ minutes }) => {
  const initialSeconds = (minutes || 0) * 60;
  const [secondsLeft, setSecondsLeft] = useState(initialSeconds);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    let interval = null;
    if (isActive && secondsLeft > 0) {
      interval = setInterval(() => {
        setSecondsLeft((sec) => sec - 1);
      }, 1000);
    } else if (secondsLeft === 0) {
      setIsActive(false);
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [isActive, secondsLeft]);

  const toggle = () => setIsActive(!isActive);
  const reset = () => {
    setIsActive(false);
    setSecondsLeft(initialSeconds);
  };

  const formatTime = (totalSec) => {
    const m = Math.floor(totalSec / 60);
    const s = totalSec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  if (!minutes || minutes <= 0) return null;

  return (
    <div style={{
      display: 'inline-flex',
      alignItems: 'center',
      gap: '0.625rem',
      backgroundColor: '#f8fafc',
      border: '1px solid var(--border)',
      padding: '0.375rem 0.75rem',
      borderRadius: '9999px',
      fontSize: '0.8125rem',
      marginTop: '0.625rem'
    }}>
      <span style={{ fontWeight: 700, fontFamily: 'monospace', fontSize: '0.875rem', color: isActive ? 'var(--primary)' : 'var(--secondary)' }}>
        ⏱️ {formatTime(secondsLeft)}
      </span>
      <button
        onClick={toggle}
        className="btn btn-sm"
        style={{ padding: '0.2rem 0.5rem', backgroundColor: isActive ? '#fef3c7' : '#ecfdf5', color: isActive ? '#b45309' : '#059669' }}
      >
        {isActive ? <Pause size={12} /> : <Play size={12} />}
        <span>{isActive ? 'Tạm dừng' : 'Bắt đầu'}</span>
      </button>
      <button onClick={reset} style={{ color: 'var(--text-muted)', display: 'flex', alignItems: 'center' }}>
        <RotateCcw size={12} />
      </button>
    </div>
  );
};

export const RecipeDetailPage = () => {
  const { slug } = useParams();
  const { user, isAdmin } = useAuth();
  const navigate = useNavigate();

  const [recipe, setRecipe] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [checkedIngredients, setCheckedIngredients] = useState({});

  useEffect(() => {
    const fetchDetail = async () => {
      setLoading(true);
      try {
        const data = await api.get(`/recipes/${slug}`);
        setRecipe(data);
      } catch (err) {
        setError(err.message || 'Không thể tải chi tiết công thức');
      } finally {
        setLoading(false);
      }
    };
    fetchDetail();
  }, [slug]);

  const toggleIngredient = (idx) => {
    setCheckedIngredients((prev) => ({
      ...prev,
      [idx]: !prev[idx],
    }));
  };

  if (loading) {
    return (
      <div className="container" style={{ padding: '6rem 0', textAlign: 'center', color: 'var(--text-muted)' }}>
        Đang tải thông tin chi tiết món ăn...
      </div>
    );
  }

  if (error || !recipe) {
    return (
      <div className="container" style={{ padding: '6rem 0', textAlign: 'center' }}>
        <h2 style={{ marginBottom: '1rem', color: '#ef4444' }}>Không tìm thấy công thức</h2>
        <p style={{ color: 'var(--text-muted)', marginBottom: '1.5rem' }}>{error}</p>
        <Link to="/recipes" className="btn btn-primary btn-sm">
          Quay lại danh sách
        </Link>
      </div>
    );
  }

  const diff = difficultyMap[recipe.difficulty] || difficultyMap[1];
  const canEdit = user && (isAdmin || user.id === recipe.author?.id);
  const imageUrl =
    recipe.primaryImage?.originalUrl ||
    recipe.images?.[0]?.originalUrl ||
    'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=1200&q=80';

  return (
    <article className="container" style={{ padding: '2.5rem 1.25rem 5rem', maxWidth: '1000px' }}>
      
      {/* Back button & Action */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem' }}>
        <Link to="/recipes" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.375rem', fontSize: '0.875rem', color: 'var(--text-muted)', fontWeight: 600 }}>
          <ArrowLeft size={16} />
          <span>Tất cả công thức</span>
        </Link>

        {canEdit && (
          <Link to={`/dashboard/recipes/${recipe.id}/edit`} className="btn btn-outline btn-sm">
            <Edit size={14} />
            <span>Chỉnh sửa công thức</span>
          </Link>
        )}
      </div>

      {/* Header Info */}
      <div style={{ marginBottom: '2rem' }}>
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '0.875rem', flexWrap: 'wrap' }}>
          {recipe.category && (
            <span style={{ backgroundColor: 'var(--primary-light)', color: 'var(--primary)', padding: '0.25rem 0.75rem', borderRadius: '9999px', fontSize: '0.75rem', fontWeight: 700, textTransform: 'uppercase' }}>
              {recipe.category.name}
            </span>
          )}
          <span className={`badge ${diff.class}`}>
            <Flame size={12} />
            Độ khó: {diff.label}
          </span>
          {recipe.status === 0 && <span className="badge badge-draft">Bản nháp (Draft)</span>}
          {recipe.status === 2 && <span className="badge badge-archived">Đã lưu trữ</span>}
        </div>

        <h1 style={{ fontSize: '2.5rem', lineHeight: 1.2, marginBottom: '1rem', color: 'var(--secondary)' }}>
          {recipe.title}
        </h1>

        <p style={{ fontSize: '1.125rem', color: 'var(--text-muted)', lineHeight: 1.6, marginBottom: '1.5rem' }}>
          {recipe.description}
        </p>

        {/* Author & Date */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
          {recipe.author && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
              <div style={{
                width: '2rem',
                height: '2rem',
                borderRadius: '50%',
                backgroundColor: 'var(--primary)',
                color: '#ffffff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 700,
                fontSize: '0.75rem'
              }}>
                {recipe.author.fullName?.charAt(0).toUpperCase()}
              </div>
              <span style={{ fontWeight: 600, color: 'var(--secondary)' }}>{recipe.author.fullName}</span>
            </div>
          )}

          <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem' }}>
            <Calendar size={15} />
            <span>{new Date(recipe.publishedAt || recipe.createdAt).toLocaleDateString('vi-VN')}</span>
          </div>
        </div>
      </div>

      {/* Main Cover Image */}
      <div style={{ borderRadius: '1.25rem', overflow: 'hidden', maxHeight: '480px', marginBottom: '2.5rem', boxShadow: '0 4px 20px rgba(0,0,0,0.06)' }}>
        <img src={imageUrl} alt={recipe.title} style={{ width: '100%', height: '100%', objectFit: 'cover', display: 'block' }} />
      </div>

      {/* Quick Recipe Meta Box */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: '1rem',
        backgroundColor: '#ffffff',
        border: '1px solid var(--border)',
        borderRadius: '1rem',
        padding: '1.5rem',
        marginBottom: '3rem',
        textAlign: 'center'
      }}>
        <div>
          <span style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, marginBottom: '0.25rem' }}>
            Chuẩn bị
          </span>
          <strong style={{ fontSize: '1.25rem', color: 'var(--secondary)' }}>{recipe.prepTime} phút</strong>
        </div>

        <div>
          <span style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, marginBottom: '0.25rem' }}>
            Thời gian nấu
          </span>
          <strong style={{ fontSize: '1.25rem', color: 'var(--secondary)' }}>{recipe.cookTime} phút</strong>
        </div>

        <div>
          <span style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, marginBottom: '0.25rem' }}>
            Tổng thời gian
          </span>
          <strong style={{ fontSize: '1.25rem', color: 'var(--primary)' }}>{recipe.prepTime + recipe.cookTime} phút</strong>
        </div>

        <div>
          <span style={{ display: 'block', fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600, marginBottom: '0.25rem' }}>
            Khẩu phần
          </span>
          <strong style={{ fontSize: '1.25rem', color: 'var(--secondary)' }}>{recipe.servings} người</strong>
        </div>
      </div>

      {/* Grid: Ingredients & Nutrition */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 0.8fr', gap: '2.5rem', marginBottom: '3.5rem' }}>
        
        {/* Ingredients Checklist */}
        <div>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.25rem' }}>
            <h2 style={{ fontSize: '1.5rem' }}>Nguyên Liệu Cần Có</h2>
            <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
              ({recipe.ingredients?.length || 0} nguyên liệu)
            </span>
          </div>

          <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', marginBottom: '1rem', fontStyle: 'italic' }}>
            💡 Mẹo: Bạn có thể bấm chọn vào nguyên liệu để đánh dấu đã chuẩn bị xong.
          </p>

          <div style={{ backgroundColor: '#ffffff', border: '1px solid var(--border)', borderRadius: '1rem', overflow: 'hidden' }}>
            {recipe.ingredients?.map((ing, idx) => {
              const isChecked = checkedIngredients[idx];
              return (
                <div
                  key={ing.id || idx}
                  onClick={() => toggleIngredient(idx)}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.875rem',
                    padding: '0.875rem 1.25rem',
                    borderBottom: idx < recipe.ingredients.length - 1 ? '1px solid var(--border)' : 'none',
                    cursor: 'pointer',
                    backgroundColor: isChecked ? '#f8fafc' : '#ffffff',
                    transition: 'background-color 0.15s'
                  }}
                >
                  {isChecked ? (
                    <CheckCircle2 size={18} color="#059669" />
                  ) : (
                    <Circle size={18} color="var(--border)" />
                  )}

                  <div style={{ flex: 1, textDecoration: isChecked ? 'line-through' : 'none', color: isChecked ? 'var(--text-muted)' : 'var(--secondary)' }}>
                    <span style={{ fontWeight: 600 }}>{ing.name}</span>
                    {ing.notes && <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginLeft: '0.5rem' }}>({ing.notes})</span>}
                  </div>

                  {ing.quantity && (
                    <span style={{ fontWeight: 700, fontSize: '0.875rem', color: isChecked ? 'var(--text-muted)' : 'var(--primary)' }}>
                      {ing.quantity} {ing.unit || ''}
                    </span>
                  )}
                </div>
              );
            })}
          </div>
        </div>

        {/* Nutrition Facts */}
        <div>
          <h2 style={{ fontSize: '1.5rem', marginBottom: '1.25rem' }}>Giá Trị Dinh Dưỡng</h2>
          
          <div style={{
            backgroundColor: '#ffffff',
            border: '1px solid var(--border)',
            borderRadius: '1rem',
            padding: '1.25rem',
            boxShadow: '0 1px 3px rgba(0,0,0,0.03)'
          }}>
            <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '1rem' }}>
              Ước tính giá trị dinh dưỡng cho mỗi khẩu phần:
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '0.5rem', borderBottom: '1px solid var(--border)', fontWeight: 700, color: 'var(--secondary)' }}>
                <span>Calories</span>
                <span style={{ color: 'var(--primary)', fontSize: '1.125rem' }}>{recipe.nutrition?.calories || 0} kcal</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '0.5rem', borderBottom: '1px solid var(--border)', fontSize: '0.875rem' }}>
                <span>Chất đạm (Protein)</span>
                <strong>{recipe.nutrition?.protein || 0} g</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '0.5rem', borderBottom: '1px solid var(--border)', fontSize: '0.875rem' }}>
                <span>Carbohydrate</span>
                <strong>{recipe.nutrition?.carbohydrates || 0} g</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '0.5rem', borderBottom: '1px solid var(--border)', fontSize: '0.875rem' }}>
                <span>Chất béo (Fat)</span>
                <strong>{recipe.nutrition?.fat || 0} g</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: '0.5rem', borderBottom: '1px solid var(--border)', fontSize: '0.875rem' }}>
                <span>Chất xơ (Fiber)</span>
                <strong>{recipe.nutrition?.fiber || 0} g</strong>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.875rem' }}>
                <span>Natri (Sodium)</span>
                <strong>{recipe.nutrition?.sodium || 0} mg</strong>
              </div>
            </div>
          </div>
        </div>

      </div>

      {/* Step by step Instructions */}
      <section style={{ marginBottom: '4rem' }}>
        <h2 style={{ fontSize: '1.75rem', marginBottom: '1.75rem' }}>Các Bước Thực Hiện</h2>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          {recipe.steps?.map((step) => (
            <div
              key={step.id || step.stepNumber}
              style={{
                backgroundColor: '#ffffff',
                border: '1px solid var(--border)',
                borderRadius: '1rem',
                padding: '1.5rem',
                display: 'flex',
                gap: '1.25rem'
              }}
            >
              {/* Step Number Circle */}
              <div style={{
                width: '2.5rem',
                height: '2.5rem',
                borderRadius: '50%',
                backgroundColor: 'var(--primary)',
                color: '#ffffff',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 800,
                fontSize: '1rem',
                flexShrink: 0
              }}>
                {step.stepNumber}
              </div>

              {/* Step Content */}
              <div style={{ flex: 1 }}>
                <h3 style={{ fontSize: '1.25rem', marginBottom: '0.5rem', color: 'var(--secondary)' }}>
                  {step.title}
                </h3>

                <p style={{ color: 'var(--text-main)', lineHeight: 1.7, fontSize: '0.9375rem', whiteSpace: 'pre-line' }}>
                  {step.description}
                </p>

                {/* Step Timer */}
                {step.timerMinutes && (
                  <CookingTimer minutes={step.timerMinutes} />
                )}
              </div>
            </div>
          ))}
        </div>
      </section>

    </article>
  );
};
