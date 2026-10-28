export const SITE_NAME = 'CulinaryBlog';
export const SITE_TAGLINE = 'Công thức nấu ăn Việt Nam và thế giới';

const getSiteUrl = () => {
  if (typeof window !== 'undefined' && window.location?.origin) {
    return window.location.origin;
  }
  return 'http://localhost:3000';
};

const compact = (object) =>
  Object.fromEntries(
    Object.entries(object).filter(([, value]) => {
      if (value === undefined || value === null || value === '') return false;
      if (Array.isArray(value) && value.length === 0) return false;
      return true;
    }),
  );

const formatNumber = (value) => {
  if (value === null || value === undefined || value === '') return null;
  const parsed = Number(value);
  if (Number.isNaN(parsed)) return null;
  return Number.isInteger(parsed) ? String(parsed) : String(parsed);
};

export const toIsoDuration = (minutes) => {
  const value = Number(minutes);
  if (!Number.isFinite(value) || value <= 0) return null;

  const hours = Math.floor(value / 60);
  const remainingMinutes = value % 60;

  let duration = 'PT';
  if (hours > 0) duration += `${hours}H`;
  if (remainingMinutes > 0 || hours === 0) duration += `${remainingMinutes}M`;
  return duration;
};

export const toAbsoluteUrl = (url, baseUrl = getSiteUrl()) => {
  if (!url) return null;
  try {
    return new URL(url, baseUrl).toString();
  } catch {
    return null;
  }
};

const buildIngredientLine = (ingredient) => {
  const quantity = formatNumber(ingredient.quantity);
  const parts = [quantity, ingredient.unit, ingredient.name].filter(Boolean);
  const line = parts.join(' ');
  return ingredient.notes ? `${line} (${ingredient.notes})` : line;
};

const buildNutrition = (nutrition) => {
  if (!nutrition) return null;

  const calories = formatNumber(nutrition.calories);
  const protein = formatNumber(nutrition.protein);
  const carbohydrates = formatNumber(nutrition.carbohydrates);
  const fat = formatNumber(nutrition.fat);
  const fiber = formatNumber(nutrition.fiber);
  const sodium = formatNumber(nutrition.sodium);

  return compact({
    '@type': 'NutritionInformation',
    calories: calories ? `${calories} kcal` : null,
    proteinContent: protein ? `${protein} g` : null,
    carbohydrateContent: carbohydrates ? `${carbohydrates} g` : null,
    fatContent: fat ? `${fat} g` : null,
    fiberContent: fiber ? `${fiber} g` : null,
    sodiumContent: sodium ? `${sodium} mg` : null,
  });
};

export const buildRecipeJsonLd = (recipe, pageUrl = getSiteUrl()) => {
  if (!recipe) return null;

  const baseUrl = getSiteUrl();

  const imageCandidates = [recipe.primaryImage, ...(recipe.images || [])]
    .filter(Boolean)
    .map((image) => toAbsoluteUrl(image.originalUrl, baseUrl))
    .filter(Boolean);
  const images = [...new Set(imageCandidates)];

  const steps = (recipe.steps || [])
    .slice()
    .sort((a, b) => (a.stepNumber || 0) - (b.stepNumber || 0))
    .map((step, index) =>
      compact({
        '@type': 'HowToStep',
        position: step.stepNumber || index + 1,
        name: step.title,
        text: step.description,
        image: toAbsoluteUrl(step.imageUrl, baseUrl),
        performTime: toIsoDuration(step.timerMinutes),
      }),
    );

  const ingredientLines = (recipe.ingredients || []).map(buildIngredientLine).filter(Boolean);

  const keywords = [
    recipe.category?.name,
    ...(recipe.ingredients || []).slice(0, 10).map((ingredient) => ingredient.name),
  ]
    .filter(Boolean)
    .join(', ');

  const author = recipe.author
    ? compact({
        '@type': 'Person',
        name: recipe.author.fullName,
        url: recipe.author.userName ? `${baseUrl}/authors/${recipe.author.userName}` : null,
      })
    : null;

  return compact({
    '@context': 'https://schema.org',
    '@type': 'Recipe',
    name: recipe.title,
    description: recipe.description,
    url: pageUrl,
    mainEntityOfPage: pageUrl,
    image: images,
    author,
    datePublished: recipe.publishedAt || recipe.createdAt || null,
    prepTime: toIsoDuration(recipe.prepTime),
    cookTime: toIsoDuration(recipe.cookTime),
    totalTime: toIsoDuration((Number(recipe.prepTime) || 0) + (Number(recipe.cookTime) || 0)),
    recipeYield: recipe.servings ? `${recipe.servings} khẩu phần` : null,
    recipeCategory: recipe.category?.name || null,
    keywords: keywords || null,
    recipeIngredient: ingredientLines,
    recipeInstructions: steps,
    nutrition: buildNutrition(recipe.nutrition),
  });
};

export const buildRecipeSeoMeta = (recipe, pageUrl = getSiteUrl()) => {
  if (!recipe) return null;

  const baseUrl = getSiteUrl();
  const imageCandidates = [recipe.primaryImage, ...(recipe.images || [])]
    .filter(Boolean)
    .map((image) => toAbsoluteUrl(image.originalUrl, baseUrl))
    .filter(Boolean);
  const primaryImage = [...new Set(imageCandidates)][0] || null;

  const description = recipe.description
    ? recipe.description.slice(0, 300)
    : `${recipe.title} - công thức nấu ăn chi tiết trên ${SITE_NAME}.`;

  return {
    title: `${recipe.title} | ${SITE_NAME}`,
    description,
    url: pageUrl,
    image: primaryImage,
    imageAlt: recipe.primaryImage?.altText || recipe.title,
    author: recipe.author?.fullName || null,
    publishedTime: recipe.publishedAt || recipe.createdAt || null,
    isPublished: recipe.status === 1,
    type: 'article',
  };
};
