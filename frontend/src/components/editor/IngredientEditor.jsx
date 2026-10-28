import { ArrowDown, ArrowUp, GripVertical, Plus, Trash2 } from 'lucide-react';
import { useDragReorder } from '../../hooks/useDragReorder';
import { createEmptyIngredient } from '../../utils/recipeForm';

export const IngredientEditor = ({ ingredients, onChange, error }) => {
  const { dragIndex, overIndex, getHandleProps, getItemProps, moveItem } =
    useDragReorder(ingredients, onChange);

  const updateIngredient = (index, field, value) => {
    onChange(
      ingredients.map((ingredient, itemIndex) =>
        itemIndex === index ? { ...ingredient, [field]: value } : ingredient,
      ),
    );
  };

  const addIngredient = () => onChange([...ingredients, createEmptyIngredient()]);

  const removeIngredient = (index) => onChange(ingredients.filter((_, itemIndex) => itemIndex !== index));

  return (
    <div>
      <div className="editor-list-actions">
        <h2 className="editor-section-title" style={{ margin: 0, border: 'none', padding: 0 }}>
          Nguyên Liệu ({ingredients.length})
        </h2>
        <button type="button" className="btn btn-outline btn-sm" onClick={addIngredient}>
          <Plus size={14} />
          <span>Thêm nguyên liệu</span>
        </button>
      </div>

      <p className="editor-tip">Giữ biểu tượng ⋮⋮ để kéo nguyên liệu lên/xuống, hoặc dùng nút mũi tên.</p>

      {error && <div className="alert alert-error" style={{ marginBottom: '1rem' }}>{error}</div>}

      {ingredients.length === 0 ? (
        <div className="empty-state">Chưa có nguyên liệu nào. Hãy thêm nguyên liệu đầu tiên.</div>
      ) : (
        <div className="editor-list">
          {ingredients.map((ingredient, index) => {
            const dragging = dragIndex === index;
            const isOver = dragIndex !== null && overIndex === index && dragIndex !== index;

            return (
              <div
                key={index}
                className={`ingredient-row${isOver ? ' drop-target' : ''}${dragging ? ' dragging' : ''}`}
                {...getItemProps(index)}
              >
                <button
                  type="button"
                  className="drag-handle"
                  title="Kéo để sắp xếp nguyên liệu"
                  aria-label={`Kéo nguyên liệu ${index + 1}`}
                  {...getHandleProps(index)}
                >
                  <GripVertical size={16} />
                </button>

                <input
                  type="text"
                  className="input"
                  placeholder="Tên nguyên liệu"
                  value={ingredient.name}
                  onChange={(event) => updateIngredient(index, 'name', event.target.value)}
                  aria-label={`Tên nguyên liệu ${index + 1}`}
                />

                <input
                  type="number"
                  min="0"
                  step="0.1"
                  className="input"
                  placeholder="Số lượng"
                  value={ingredient.quantity}
                  onChange={(event) => updateIngredient(index, 'quantity', event.target.value)}
                  aria-label={`Số lượng nguyên liệu ${index + 1}`}
                />

                <input
                  type="text"
                  className="input"
                  placeholder="Đơn vị"
                  value={ingredient.unit}
                  onChange={(event) => updateIngredient(index, 'unit', event.target.value)}
                  aria-label={`Đơn vị nguyên liệu ${index + 1}`}
                />

                <input
                  type="text"
                  className="input"
                  placeholder="Ghi chú (tùy chọn)"
                  value={ingredient.notes}
                  onChange={(event) => updateIngredient(index, 'notes', event.target.value)}
                  aria-label={`Ghi chú nguyên liệu ${index + 1}`}
                />

                <div className="move-stack">
                  <button
                    type="button"
                    className="move-btn"
                    onClick={() => moveItem(index, index - 1)}
                    disabled={index === 0}
                    title="Di chuyển lên"
                    aria-label={`Di chuyển nguyên liệu ${index + 1} lên`}
                  >
                    <ArrowUp size={12} />
                  </button>
                  <button
                    type="button"
                    className="move-btn"
                    onClick={() => moveItem(index, index + 1)}
                    disabled={index === ingredients.length - 1}
                    title="Di chuyển xuống"
                    aria-label={`Di chuyển nguyên liệu ${index + 1} xuống`}
                  >
                    <ArrowDown size={12} />
                  </button>
                </div>

                <button
                  type="button"
                  className="icon-btn danger"
                  onClick={() => removeIngredient(index)}
                  title="Xóa nguyên liệu"
                  aria-label={`Xóa nguyên liệu ${index + 1}`}
                >
                  <Trash2 size={16} />
                </button>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
