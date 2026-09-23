import React from 'react';
import { Link } from 'react-router-dom';
import { Clock, Users, Flame } from 'lucide-react';

const difficultyMap = {
  1: { label: 'Dễ', class: 'badge-easy' },
  2: { label: 'Vừa', class: 'badge-medium' },
  3: { label: 'Khó', class: 'badge-hard' },
  4: { label: 'Bếp trưởng', class: 'badge-expert' },
};

export const RecipeCard = ({ recipe }) => {
  const diff = difficultyMap[recipe.difficulty] || difficultyMap[1];
  const totalTime = (recipe.prepTime || 0) + (recipe.cookTime || 0);

  // Fallback image based on title or food theme
  const imageUrl =
    recipe.primaryImage?.originalUrl ||
    recipe.primaryImage?.mediumUrl ||
    'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80';

  return (
    <div className="card" style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      {/* Image container */}
      <Link to={`/recipes/${recipe.slug}`} style={{ position: 'relative', width: '100%', paddingTop: '65%', overflow: 'hidden', display: 'block', backgroundColor: '#f1f5f9' }}>
        <img
          src={imageUrl}
          alt={recipe.title}
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            objectFit: 'cover',
            transition: 'transform 0.4s ease',
          }}
          onMouseOver={(e) => (e.currentTarget.style.transform = 'scale(1.05)')}
          onMouseOut={(e) => (e.currentTarget.style.transform = 'scale(1)')}
        />
        {/* Category tag */}
        {recipe.category && (
          <div style={{ position: 'absolute', top: '0.75rem', left: '0.75rem' }}>
            <span style={{
              backgroundColor: 'rgba(15, 23, 42, 0.75)',
              backdropFilter: 'blur(4px)',
              color: '#ffffff',
              padding: '0.25rem 0.625rem',
              borderRadius: '9999px',
              fontSize: '0.6875rem',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.05em'
            }}>
              {recipe.category.name}
            </span>
          </div>
        )}

        {/* Difficulty badge */}
        <div style={{ position: 'absolute', top: '0.75rem', right: '0.75rem' }}>
          <span className={`badge ${diff.class}`}>
            <Flame size={12} />
            {diff.label}
          </span>
        </div>
      </Link>

      {/* Content */}
      <div style={{ padding: '1.25rem', display: 'flex', flexDirection: 'column', flex: 1 }}>
        <Link to={`/recipes/${recipe.slug}`}>
          <h3 style={{ fontSize: '1.125rem', lineHeight: 1.4, marginBottom: '0.5rem', color: 'var(--secondary)' }}>
            {recipe.title}
          </h3>
        </Link>

        <p style={{
          fontSize: '0.8125rem',
          color: 'var(--text-muted)',
          lineHeight: 1.5,
          marginBottom: '1rem',
          display: '-webkit-box',
          WebkitLineClamp: 2,
          WebkitBoxOrient: 'vertical',
          overflow: 'hidden',
          textOverflow: 'ellipsis',
          flex: 1
        }}>
          {recipe.description}
        </p>

        {/* Recipe Meta Info */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          borderTop: '1px solid var(--border)',
          paddingTop: '0.875rem',
          fontSize: '0.75rem',
          color: 'var(--text-muted)',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem' }}>
            <Clock size={14} color="var(--primary)" />
            <span>{totalTime} phút</span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem' }}>
            <Users size={14} />
            <span>{recipe.servings} người</span>
          </div>

          {recipe.author && (
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem' }}>
              <div style={{
                width: '1.25rem',
                height: '1.25rem',
                borderRadius: '50%',
                backgroundColor: 'var(--primary-light)',
                color: 'var(--primary)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '0.625rem',
                fontWeight: 700
              }}>
                {recipe.author.fullName?.charAt(0).toUpperCase() || 'A'}
              </div>
              <span style={{ maxWidth: '5rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                {recipe.author.fullName}
              </span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
