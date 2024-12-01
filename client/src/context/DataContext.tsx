import React, { createContext, useContext, useState } from "react";
import { IPreson } from "../interfaces/IPerson";

interface IDataContext {
  cards: IPreson | null;
  setCards: React.Dispatch<React.SetStateAction<IPreson | null>>;
  isSearch: boolean;
  setIsSearch: React.Dispatch<React.SetStateAction<boolean>>;
  inputValue: string;
  setInputValue: React.Dispatch<React.SetStateAction<string>>;
}

const DataContext = createContext<IDataContext | undefined>(undefined);

export const DataProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [cards, setCards] = useState<IPreson | null>(null);
  const [isSearch, setIsSearch] = useState(false);
  const [inputValue, setInputValue] = useState<string>("");

  return (
    <DataContext.Provider
      value={{
        cards,
        setCards,
        isSearch,
        setIsSearch,
        inputValue,
        setInputValue,
      }}
    >
      {children}
    </DataContext.Provider>
  );
};

export const useCards = () => {
  const context = useContext(DataContext);
  if (!context) {
    throw new Error("useData must be used within a DataProvider");
  }
  return context;
};
