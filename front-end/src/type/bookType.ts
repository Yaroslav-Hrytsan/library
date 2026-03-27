import type { CategoryIdType } from "./categoryType";

export interface BookType {
  id: number;
  title: string;
  category: CategoryIdType;
  author: string;
  year: number;
  rating: number;
  pages: number;
  description: string;
  cover: string;
  views: number;
  
}