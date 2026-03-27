import React from "react";

interface SearchContextType {
  valueInput: string,
  setValueInput: (valueInput: string) => void;
}

const searchValue: SearchContextType = {
  valueInput: "",
  setValueInput: () => {},
};

// eslint-disable-next-line react-refresh/only-export-components
export const SearchContext = React.createContext<SearchContextType>(searchValue);

export const SearchProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [valueInput, setValueInput] = React.useState("");
  const value = { valueInput, setValueInput };
  return (
    <SearchContext.Provider value={value}>
      {children}
    </SearchContext.Provider>
  );
};

// eslint-disable-next-line react-refresh/only-export-components
export const useSearch = () => {
  const context = React.useContext(SearchContext);
  if (!context) {
    throw new Error("useSearch must be used within SearchProvider");
  }
  return context;
};