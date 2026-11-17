/**
 * TypeScript Type Definitions for Culinary Blog Frontend
 * Generated & Standardized based on SRS v1.0.0 and Backend OpenAPI Schemas
 */

// ==========================================
// 1. Common & Utility Types
// ==========================================

export interface PagedMeta {
  page: number;
  pageSize: number;
  total: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPreviousPage: boolean;
}

export interface PagedResult<T> {
  items: T[];
  meta: PagedMeta;
}

export interface ProblemDetails {
  type: string;
  title: string;
  status: number;
  detail: string;
  errors?: Record<string, string[]>;
}

export interface ApiResponse<T = any> {
  data?: T;
  message?: string;
  error?: ProblemDetails;
}

// ==========================================
// 2. Authentication & User Profile Types
// ==========================================

export type UserRole = 'Author' | 'Admin';

export interface UserProfile {
  id: string;
  fullName: string;
  email: string;
  userName: string;
  avatarUrl?: string | null;
  bio?: string | null;
  roles: UserRole[];
  emailConfirmed: boolean;
  createdAt: string;
}

export interface AuthTokens {
  accessToken: string;
  refreshToken: string;
  expiresIn: number; // in seconds (default: 900 = 15m)
}

export interface AuthResponseDto extends AuthTokens {
  user: UserProfile;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  fullName: string;
  email: string;
  userName: string;
  password: string;
}

export interface GoogleLoginRequest {
  idToken: string;
}

export interface RefreshTokenRequest {
  refreshToken: string;
}

export interface UpdateProfileRequest {
  fullName?: string;
  avatarUrl?: string | null;
  bio?: string | null;
}

// ==========================================
// 3. Category Types
// ==========================================

export interface CategoryBase {
  name: string;
  description?: string | null;
  imageUrl?: string | null;
  orderIndex: number;
}

export interface Category extends CategoryBase {
  id: string;
  slug: string;
  recipeCount: number;
}

export interface CategorySummary {
  id: string;
  name: string;
  slug: string;
}

export interface CategoryCreateRequest extends CategoryBase {}

export interface CategoryUpdateRequest {
  name?: string;
  description?: string | null;
  imageUrl?: string | null;
  orderIndex?: number;
}

// ==========================================
// 4. Recipe Enums & Sub-entity Types
// ==========================================

export enum RecipeDifficulty {
  Easy = 1,
  Medium = 2,
  Hard = 3,
  Master = 4,
}

export enum RecipeStatus {
  Draft = 0,
  Published = 1,
  Archived = 2,
}

export interface RecipeNutrition {
  calories?: number | null;
  protein?: number | null;
  carbohydrates?: number | null;
  fat?: number | null;
  fiber?: number | null;
  sodium?: number | null;
}

export interface RecipeAuthor {
  id: string;
  fullName: string;
  userName: string;
  avatarUrl?: string | null;
}

export interface RecipeImage {
  id: string;
  originalUrl: string;
  mediumUrl?: string | null;
  thumbnailUrl?: string | null;
  altText?: string | null;
  isPrimary: boolean;
  orderIndex: number;
}

export interface RecipeIngredient {
  id: string;
  name: string;
  quantity?: number | null;
  unit?: string | null;
  notes?: string | null;
  orderIndex: number;
}

export interface RecipeIngredientCreate {
  name: string;
  quantity?: number | null;
  unit?: string | null;
  notes?: string | null;
  orderIndex?: number;
}

export interface RecipeStep {
  id: string;
  stepNumber: number;
  title: string;
  description: string;
  timerMinutes?: number | null;
  imageUrl?: string | null;
}

export interface RecipeStepCreate {
  title: string;
  description: string;
  timerMinutes?: number | null;
  imageUrl?: string | null;
}

// ==========================================
// 5. Recipe Core Types & DTOs
// ==========================================

export interface RecipeSummary {
  id: string;
  title: string;
  slug: string;
  description: string;
  prepTime: number;
  cookTime: number;
  servings: number;
  difficulty: RecipeDifficulty;
  status: RecipeStatus;
  category?: CategorySummary | null;
  author?: RecipeAuthor | null;
  primaryImage?: RecipeImage | null;
  publishedAt?: string | null;
  createdAt: string;
}

export interface RecipeDetail extends RecipeSummary {
  instructions: string;
  nutrition?: RecipeNutrition | null;
  steps: RecipeStep[];
  ingredients: RecipeIngredient[];
  images: RecipeImage[];
  rowVersion: number;
}

export interface RecipeCreateRequest {
  title: string;
  description: string;
  categoryId: string;
  prepTimeMinutes: number;
  cookTimeMinutes: number;
  servings: number;
  difficulty: RecipeDifficulty;
  instructions?: string;
  nutrition?: RecipeNutrition;
  steps?: RecipeStepCreate[];
  ingredients?: RecipeIngredientCreate[];
}

export interface RecipeUpdateRequest {
  title?: string;
  description?: string;
  categoryId?: string;
  prepTimeMinutes?: number;
  cookTimeMinutes?: number;
  servings?: number;
  difficulty?: RecipeDifficulty;
  instructions?: string;
  nutrition?: RecipeNutrition;
  rowVersion?: number;
}

export interface RecipeFilterParams {
  page?: number;
  pageSize?: number;
  categoryId?: string;
  difficulty?: RecipeDifficulty;
  status?: RecipeStatus;
  mine?: boolean;
  search?: string;
  sortBy?: 'createdAt' | 'title' | 'cookTime';
  sortOrder?: 'asc' | 'desc';
}

// ==========================================
// 6. Creator Dashboard Types
// ==========================================

export interface RecentRecipeItem {
  id: string;
  title: string;
  slug: string;
  status: RecipeStatus;
  category: string;
  createdAt: string;
  primaryImageUrl?: string | null;
}

export interface CategoryDistributionItem {
  categoryId: string;
  categoryName: string;
  categorySlug: string;
  recipeCount: number;
}

export interface DifficultyDistributionItem {
  difficulty: RecipeDifficulty;
  difficultyLabel: string;
  count: number;
}

export interface DashboardStats {
  totalRecipes: number;
  publishedCount: number;
  draftCount: number;
  archivedCount: number;
  recentRecipes: RecentRecipeItem[];
  categoryDistribution: CategoryDistributionItem[];
  difficultyDistribution: DifficultyDistributionItem[];
}
