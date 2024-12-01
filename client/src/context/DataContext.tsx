import React, { createContext, useContext, useState } from "react";
import { IPreson } from "../interfaces/IPerson";

interface IDataContext {
  cards: IPreson | null;
  setCards: React.Dispatch<React.SetStateAction<IPreson | null>>;
}

const DataContext = createContext<IDataContext | undefined>(undefined);

export const DataProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [cards, setCards] = useState<IPreson | null>(null);

  return (
    <DataContext.Provider value={{ cards, setCards }}>
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
