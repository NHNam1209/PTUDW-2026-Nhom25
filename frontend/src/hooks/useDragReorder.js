import { useState } from 'react';

export const useDragReorder = (items, onChange) => {
  const [dragIndex, setDragIndex] = useState(null);
  const [overIndex, setOverIndex] = useState(null);

  const resetDrag = () => {
    setDragIndex(null);
    setOverIndex(null);
  };

  const moveItem = (from, to) => {
    if (from === null || to === null || from === to) return;
    if (from < 0 || to < 0 || from >= items.length || to >= items.length) return;

    const next = [...items];
    const [moved] = next.splice(from, 1);
    next.splice(to, 0, moved);
    onChange(next);
  };

  const getHandleProps = (index) => ({
    draggable: true,
    onDragStart: (event) => {
      event.dataTransfer.effectAllowed = 'move';
      event.dataTransfer.setData('text/plain', String(index));
      setDragIndex(index);
    },
    onDragEnd: resetDrag,
  });

  const getItemProps = (index) => ({
    onDragOver: (event) => {
      if (dragIndex === null) return;
      event.preventDefault();
      event.dataTransfer.dropEffect = 'move';
      setOverIndex(index);
    },
    onDragLeave: () => {
      setOverIndex((current) => (current === index ? null : current));
    },
    onDrop: (event) => {
      event.preventDefault();
      moveItem(dragIndex, index);
      resetDrag();
    },
  });

  return {
    dragIndex,
    overIndex,
    getHandleProps,
    getItemProps,
    moveItem,
    resetDrag,
    isDragging: dragIndex !== null,
  };
};
