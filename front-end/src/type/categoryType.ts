export type CategoryIdType =
  | "all-books"
  | "fiction"
  | "fantasy"
  | "sci-fi"
  | "psychology"
  | "business"
  | "self-dev"
  | "history"
  | "classic";

export interface CategoryType {
    id: CategoryIdType
    name: string
}