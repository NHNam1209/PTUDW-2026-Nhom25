import { api } from '../api/client';
import { buildIngredientPayload, buildStepPayload } from './recipeForm';

const stepsOrderChanged = (originalSteps, currentSteps) => {
  const currentIds = currentSteps.filter((step) => step.id).map((step) => step.id);
  const keptOriginalIds = originalSteps
    .map((step) => step.id)
    .filter((id) => currentIds.includes(id));

  if (currentIds.join('|') !== keptOriginalIds.join('|')) {
    return true;
  }

  const firstNewIndex = currentSteps.findIndex((step) => !step.id);
  if (firstNewIndex !== -1 && currentSteps.slice(firstNewIndex).some((step) => step.id)) {
    return true;
  }

  return false;
};

export const uploadQueuedImages = async (recipeId, pendingImages, coverKey, onProgress) => {
  const uploaded = [];

  for (let index = 0; index < pendingImages.length; index += 1) {
    const item = pendingImages[index];
    const formData = new FormData();
    formData.append('file', item.file);

    if (item.altText) {
      formData.append('altText', item.altText);
    }

    const isCover = coverKey === `pending:${item.uid}` || (!coverKey && index === 0);
    formData.append('isPrimary', String(isCover));

    const image = await api.upload(`/recipes/${recipeId}/images`, formData, (percent) => {
      if (onProgress) onProgress(item.uid, percent);
    });

    uploaded.push(image);
  }

  return uploaded;
};

export const setPrimaryImage = (recipeId, imageId) => api.patch(`/recipes/${recipeId}/images/${imageId}/primary`);

export const syncIngredients = async (recipeId, originalIngredients, currentIngredients) => {
  const currentIds = new Set(currentIngredients.filter((item) => item.id).map((item) => item.id));

  for (const ingredient of originalIngredients) {
    if (!currentIds.has(ingredient.id)) {
      await api.delete(`/recipes/${recipeId}/ingredients/${ingredient.id}`);
    }
  }

  for (let index = 0; index < currentIngredients.length; index += 1) {
    const ingredient = currentIngredients[index];
    const payload = buildIngredientPayload(ingredient, index);

    if (ingredient.id) {
      await api.put(`/recipes/${recipeId}/ingredients/${ingredient.id}`, payload);
    } else {
      await api.post(`/recipes/${recipeId}/ingredients`, payload);
    }
  }
};

export const syncSteps = async (recipeId, originalSteps, currentSteps) => {
  // The steps API has no endpoint to change stepNumber, so any reorder is
  // persisted by replacing the whole collection in the desired order.
  if (stepsOrderChanged(originalSteps, currentSteps)) {
    for (const step of originalSteps) {
      await api.delete(`/recipes/${recipeId}/steps/${step.id}`);
    }
    for (const step of currentSteps) {
      await api.post(`/recipes/${recipeId}/steps`, buildStepPayload(step));
    }
    return;
  }

  const currentIds = new Set(currentSteps.filter((step) => step.id).map((step) => step.id));

  for (const step of originalSteps) {
    if (!currentIds.has(step.id)) {
      await api.delete(`/recipes/${recipeId}/steps/${step.id}`);
    }
  }

  for (const step of currentSteps) {
    const payload = buildStepPayload(step);

    if (step.id) {
      await api.put(`/recipes/${recipeId}/steps/${step.id}`, payload);
    } else {
      await api.post(`/recipes/${recipeId}/steps`, payload);
    }
  }
};
