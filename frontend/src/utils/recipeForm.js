export const DIFFICULTY_OPTIONS = [
  { value: 1, label: 'Dễ' },
  { value: 2, label: 'Trung bình' },
  { value: 3, label: 'Khó' },
  { value: 4, label: 'Bếp trưởng' },
];

export const STATUS_LABELS = {
  0: 'Bản nháp',
  1: 'Đã xuất bản',
  2: 'Đã lưu trữ',
};

const toNumberOrNull = (value) => {
  if (value === '' || value === null || value === undefined) return null;
  const parsed = Number(value);
  return Number.isNaN(parsed) ? null : parsed;
};

export const createEmptyForm = () => ({
  title: '',
  description: '',
  categoryId: '',
  difficulty: 1,
  servings: 4,
  prepTimeMinutes: 30,
  cookTimeMinutes: 30,
  instructions: '',
  calories: '',
  protein: '',
  carbohydrates: '',
  fat: '',
  fiber: '',
  sodium: '',
});

export const formFromRecipe = (recipe) => ({
  title: recipe.title || '',
  description: recipe.description || '',
  categoryId: recipe.category?.id || recipe.categoryId || '',
  difficulty: recipe.difficulty || 1,
  servings: recipe.servings ?? 4,
  prepTimeMinutes: recipe.prepTime ?? 30,
  cookTimeMinutes: recipe.cookTime ?? 0,
  instructions: recipe.instructions || '',
  calories: recipe.nutrition?.calories ?? '',
  protein: recipe.nutrition?.protein ?? '',
  carbohydrates: recipe.nutrition?.carbohydrates ?? '',
  fat: recipe.nutrition?.fat ?? '',
  fiber: recipe.nutrition?.fiber ?? '',
  sodium: recipe.nutrition?.sodium ?? '',
});

export const createEmptyIngredient = () => ({
  name: '',
  quantity: '',
  unit: '',
  notes: '',
});

export const createEmptyStep = (index = 0) => ({
  title: index === 0 ? 'Sơ chế nguyên liệu' : `Bước ${index + 1}`,
  description: '',
  timerMinutes: '',
});

export const ingredientsFromRecipe = (recipe = {}) =>
  (recipe.ingredients || []).map((ing) => ({
    id: ing.id,
    name: ing.name || '',
    quantity: ing.quantity === null || ing.quantity === undefined ? '' : Number(ing.quantity),
    unit: ing.unit || '',
    notes: ing.notes || '',
  }));

export const stepsFromRecipe = (recipe = {}) =>
  (recipe.steps || [])
    .slice()
    .sort((a, b) => (a.stepNumber || 0) - (b.stepNumber || 0))
    .map((step) => ({
      id: step.id,
      title: step.title || '',
      description: step.description || '',
      timerMinutes: step.timerMinutes ?? '',
      imageUrl: step.imageUrl || null,
    }));

export const validateInfoStep = (form) => {
  const errors = {};

  const title = form.title.trim();
  if (title.length < 5) errors.title = 'Tên món ăn phải có ít nhất 5 ký tự.';
  else if (title.length > 200) errors.title = 'Tên món ăn không được vượt quá 200 ký tự.';

  const description = form.description.trim();
  if (description.length < 10) errors.description = 'Mô tả phải có ít nhất 10 ký tự.';
  else if (description.length > 2000) errors.description = 'Mô tả không được vượt quá 2000 ký tự.';

  if (!form.categoryId) errors.categoryId = 'Vui lòng chọn danh mục cho công thức.';

  const prep = Number(form.prepTimeMinutes);
  if (!Number.isInteger(prep) || prep <= 0) {
    errors.prepTimeMinutes = 'Thời gian chuẩn bị phải là số nguyên lớn hơn 0.';
  }

  const cook = Number(form.cookTimeMinutes);
  if (!Number.isInteger(cook) || cook < 0) {
    errors.cookTimeMinutes = 'Thời gian nấu phải là số nguyên không âm.';
  }

  const servings = Number(form.servings);
  if (!Number.isInteger(servings) || servings <= 0) {
    errors.servings = 'Khẩu phần phải là số nguyên lớn hơn 0.';
  }

  return errors;
};

export const validateNutrition = (form) => {
  const fields = ['calories', 'protein', 'carbohydrates', 'fat', 'fiber', 'sodium'];
  const errors = {};

  fields.forEach((field) => {
    const raw = form[field];
    if (raw === '' || raw === null || raw === undefined) return;
    const value = Number(raw);
    if (Number.isNaN(value) || value < 0) {
      errors[field] = 'Giá trị dinh dưỡng phải là số không âm.';
    }
  });

  return errors;
};

export const validateIngredients = (ingredients) => {
  if (ingredients.length === 0) {
    return 'Công thức cần ít nhất một nguyên liệu.';
  }

  for (let index = 0; index < ingredients.length; index += 1) {
    const ingredient = ingredients[index];
    const position = index + 1;

    if (!ingredient.name.trim()) {
      return `Nguyên liệu #${position}: vui lòng nhập tên nguyên liệu.`;
    }
    if (ingredient.name.trim().length > 200) {
      return `Nguyên liệu #${position}: tên không được vượt quá 200 ký tự.`;
    }
    if (ingredient.quantity !== '' && Number(ingredient.quantity) < 0) {
      return `Nguyên liệu #${position}: số lượng không hợp lệ.`;
    }
  }

  return null;
};

export const validateSteps = (steps) => {
  if (steps.length === 0) {
    return 'Công thức cần ít nhất một bước thực hiện.';
  }

  for (let index = 0; index < steps.length; index += 1) {
    const step = steps[index];
    const position = index + 1;

    if (step.title.trim().length < 2) {
      return `Bước ${position}: tiêu đề phải có ít nhất 2 ký tự.`;
    }
    if (step.title.trim().length > 200) {
      return `Bước ${position}: tiêu đề không được vượt quá 200 ký tự.`;
    }
    if (step.description.trim().length < 5) {
      return `Bước ${position}: mô tả phải có ít nhất 5 ký tự.`;
    }
    if (step.timerMinutes !== '' && Number(step.timerMinutes) < 0) {
      return `Bước ${position}: thời gian hẹn giờ không hợp lệ.`;
    }
  }

  return null;
};

export const buildRecipePayload = (form) => ({
  title: form.title.trim(),
  description: form.description.trim(),
  categoryId: form.categoryId,
  difficulty: Number(form.difficulty),
  prepTimeMinutes: Number(form.prepTimeMinutes),
  cookTimeMinutes: Number(form.cookTimeMinutes),
  servings: Number(form.servings),
  instructions: form.instructions.trim(),
  nutrition: {
    calories: toNumberOrNull(form.calories),
    protein: toNumberOrNull(form.protein),
    carbohydrates: toNumberOrNull(form.carbohydrates),
    fat: toNumberOrNull(form.fat),
    fiber: toNumberOrNull(form.fiber),
    sodium: toNumberOrNull(form.sodium),
  },
});

export const buildIngredientPayload = (ingredient, orderIndex) => ({
  name: ingredient.name.trim(),
  quantity: toNumberOrNull(ingredient.quantity),
  unit: ingredient.unit.trim() || null,
  notes: ingredient.notes.trim() || null,
  orderIndex,
});

export const buildStepPayload = (step) => ({
  title: step.title.trim(),
  description: step.description.trim(),
  timerMinutes: toNumberOrNull(step.timerMinutes) ?? 0,
  imageUrl: step.imageUrl || null,
});

export const formatMinutes = (minutes) => {
  const value = Number(minutes) || 0;
  if (value < 60) return `${value} phút`;
  const hours = Math.floor(value / 60);
  const rest = value % 60;
  return rest ? `${hours} giờ ${rest} phút` : `${hours} giờ`;
};
