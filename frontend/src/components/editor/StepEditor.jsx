import { ArrowDown, ArrowUp, Clock, GripVertical, Plus, Trash2 } from 'lucide-react';
import { useDragReorder } from '../../hooks/useDragReorder';
import { createEmptyStep } from '../../utils/recipeForm';

export const StepEditor = ({ steps, onChange, error }) => {
  const { dragIndex, overIndex, getHandleProps, getItemProps, moveItem } = useDragReorder(steps, onChange);

  const updateStep = (index, field, value) => {
    onChange(steps.map((step, itemIndex) => (itemIndex === index ? { ...step, [field]: value } : step)));
  };

  const addStep = () => onChange([...steps, createEmptyStep(steps.length)]);

  const removeStep = (index) => onChange(steps.filter((_, itemIndex) => itemIndex !== index));

  return (
    <div>
      <div className="editor-list-actions">
        <h2 className="editor-section-title" style={{ margin: 0, border: 'none', padding: 0 }}>
          Các Bước Thực Hiện ({steps.length})
        </h2>
        <button type="button" className="btn btn-outline btn-sm" onClick={addStep}>
          <Plus size={14} />
          <span>Thêm bước</span>
        </button>
      </div>

      <p className="editor-tip">
        Kéo thả các bước để thay đổi thứ tự thực hiện. Số thứ tự được đánh lại tự động khi lưu.
      </p>

      {error && <div className="alert alert-error" style={{ marginBottom: '1rem' }}>{error}</div>}

      {steps.length === 0 ? (
        <div className="empty-state">Chưa có bước nào. Hãy thêm bước thực hiện đầu tiên.</div>
      ) : (
        <div className="editor-list">
          {steps.map((step, index) => {
            const dragging = dragIndex === index;
            const isOver = dragIndex !== null && overIndex === index && dragIndex !== index;

            return (
              <div
                key={index}
                className={`item-card step-card${isOver ? ' drop-target' : ''}${dragging ? ' dragging' : ''}`}
                {...getItemProps(index)}
              >
                <div className="step-head">
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <button
                      type="button"
                      className="drag-handle"
                      title="Kéo để đổi thứ tự bước"
                      aria-label={`Kéo bước ${index + 1}`}
                      {...getHandleProps(index)}
                    >
                      <GripVertical size={16} />
                    </button>
                    <span className="step-badge">Bước {index + 1}</span>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.375rem' }}>
                    <div className="move-stack">
                      <button
                        type="button"
                        className="move-btn"
                        onClick={() => moveItem(index, index - 1)}
                        disabled={index === 0}
                        title="Đưa bước lên"
                        aria-label={`Đưa bước ${index + 1} lên`}
                      >
                        <ArrowUp size={12} />
                      </button>
                      <button
                        type="button"
                        className="move-btn"
                        onClick={() => moveItem(index, index + 1)}
                        disabled={index === steps.length - 1}
                        title="Đưa bước xuống"
                        aria-label={`Đưa bước ${index + 1} xuống`}
                      >
                        <ArrowDown size={12} />
                      </button>
                    </div>

                    <button
                      type="button"
                      className="icon-btn danger"
                      onClick={() => removeStep(index)}
                      title="Xóa bước"
                      aria-label={`Xóa bước ${index + 1}`}
                    >
                      <Trash2 size={16} />
                    </button>
                  </div>
                </div>

                <div className="editor-grid" style={{ marginBottom: '1rem' }}>
                  <div className="field" style={{ margin: 0 }}>
                    <label className="field-label" htmlFor={`step-title-${index}`}>Tiêu đề bước *</label>
                    <input
                      id={`step-title-${index}`}
                      type="text"
                      className="input"
                      placeholder="VD: Xào sơ thịt bò với lửa lớn"
                      value={step.title}
                      onChange={(event) => updateStep(index, 'title', event.target.value)}
                    />
                  </div>

                  <div className="field" style={{ margin: 0 }}>
                    <label className="field-label" htmlFor={`step-timer-${index}`}>
                      <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.25rem' }}>
                        <Clock size={13} /> Hẹn giờ (phút)
                      </span>
                    </label>
                    <input
                      id={`step-timer-${index}`}
                      type="number"
                      min="0"
                      className="input"
                      placeholder="0 = không cần"
                      value={step.timerMinutes}
                      onChange={(event) => updateStep(index, 'timerMinutes', event.target.value)}
                    />
                  </div>
                </div>

                <div className="field">
                  <label className="field-label" htmlFor={`step-description-${index}`}>Mô tả chi tiết *</label>
                  <textarea
                    id={`step-description-${index}`}
                    rows={3}
                    className="textarea"
                    placeholder="Mô tả kỹ thuật nấu, nhiệt độ, dấu hiệu món ăn đạt yêu cầu..."
                    value={step.description}
                    onChange={(event) => updateStep(index, 'description', event.target.value)}
                  />
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
