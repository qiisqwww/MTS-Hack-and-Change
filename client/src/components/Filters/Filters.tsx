import { useEffect, useRef, useState } from "react";
import Filter from "../Filter/Filter";
import Title from "../Title/Title";
import styles from "./Filters.module.css";
import axios, { AxiosError } from "axios";
// import { useStore } from "zustand";
import { IPreson } from "../../interfaces/IPerson";
import { useCards } from "../../context/DataContext";

interface IDepartment {
  id: number;
  name: string;
  path: string;
}

export interface IPosts {
  id: number;
  name: string;
  role_id: number;
}

export interface IRoles {
  id: number;
  name: string;
}

interface IFilterData {
  departments: IDepartment[];
  posts_and_roles: {
    posts: IPosts[];
    roles: IRoles[];
  };
}

export default function Filters() {
  const [data, setData] = useState<IFilterData | null>(null);
  const [departments, setDepartments] = useState<
    { id: number; name: string }[][]
  >([]);
  const { setCards, setIsSearch, inputValue } = useCards();

  const refs = useRef<{
    [key: string]: HTMLInputElement | HTMLSelectElement | null;
  }>({});

  const loadFilters = async () => {
    try {
      const response = await axios.get<IFilterData>(
        `${import.meta.env.VITE_API_URL}/info`
      );
      setData(response.data);
    } catch (error: unknown) {
      const e = error as AxiosError;
      console.error(e);
    }
  };

  useEffect(() => {
    loadFilters();
  }, []);

  useEffect(() => {
    if (data?.departments) {
      const newDepartments: { id: number; name: string }[][] = [];
      data.departments.forEach((depart) => {
        const level = depart.path.split("/").length;
        if (!newDepartments[level]) {
          newDepartments[level] = [];
        }
        newDepartments[level].push({ id: depart.id, name: depart.name });
      });
      setDepartments(newDepartments);
      handleReset();
    }
  }, [data]);

  const handleApply = async () => {
    const result: Record<string, string | number> = {};

    Object.keys(refs.current).forEach((key) => {
      const element = refs.current[key];
      if (element instanceof HTMLInputElement) {
        result[key] = element.value.trim();
      } else if (element instanceof HTMLSelectElement) {
        result[key] = element.value;
      }
    });
    console.log(result);
    let departmentNumber;
    if (result.departament5) {
      departmentNumber = result.departament5;
    } else if (result.departament4) {
      departmentNumber = result.departament4;
    } else if (result.departament3) {
      departmentNumber = result.departament3;
    } else if (result.departament2) {
      departmentNumber = result.departament2;
    } else if (result.departament1) {
      departmentNumber = result.departament1;
    }
    console.log(data?.departments, departmentNumber);
    const params = {
      department_name: departmentNumber
        ? data?.departments[Number(departmentNumber) - 2].name
        : null,
      post: result.post
        ? data?.posts_and_roles.posts[Number(result.post) - 2].name
        : null,
      role: result.role
        ? data?.posts_and_roles.roles[Number(result.role) - 2].name
        : null,
      first_name: result.first_name,
      last_name: result.last_name,
      phone_number: result.phone,
      city: result.city,
      adress: result.adress,
      email: result.email,
      tg_username: result.telegram,
      prompt: inputValue,
    };

    console.log(params);

    const filteredParams = Object.fromEntries(
      Object.entries(params).filter(
        // eslint-disable-next-line @typescript-eslint/no-unused-vars
        ([_, value]) => value != null && value !== ""
      )
    );

    try {
      const response = await axios.get<IPreson[]>(
        `${import.meta.env.VITE_API_URL}/filter`,
        {
          params: filteredParams,
        }
      );
      console.log(response.data);
      setCards(response.data);
      setIsSearch(true);
    } catch (error: unknown) {
      const e = error as AxiosError;
      console.error(e);
    }
  };

  const handleReset = () => {
    Object.keys(refs.current).forEach((key) => {
      const element = refs.current[key];
      if (
        element instanceof HTMLInputElement ||
        element instanceof HTMLSelectElement
      ) {
        element.value = "";
      }
    });
  };

  return (
    <div className={styles.filters}>
      <Title title="SEARCH CRITERIA" />
      <ul className={styles.list}>
        <Filter
          title="Department №1"
          isList={true}
          options={departments[1] || []}
          inputRef={(el) => (refs.current["departament1"] = el)}
        />
        <Filter
          title="Functional block"
          isList={true}
          options={departments[2] || []}
          inputRef={(el) => (refs.current["departament2"] = el)}
        />
        <Filter
          title="Department №2"
          isList={true}
          options={departments[3] || []}
          inputRef={(el) => (refs.current["departament3"] = el)}
        />
        <Filter
          title="Department №3"
          isList={true}
          options={departments[4] || []}
          inputRef={(el) => (refs.current["departament4"] = el)}
        />
        <Filter
          title="Department №4"
          isList={true}
          options={departments[5] || []}
          inputRef={(el) => (refs.current["departament5"] = el)}
        />
        <Filter
          title="Post"
          isList={true}
          options={data ? data.posts_and_roles.posts : []}
          inputRef={(el) => (refs.current["post"] = el)}
        />
        <Filter
          title="Роль"
          isList={true}
          options={data ? data.posts_and_roles.roles : []}
          inputRef={(el) => (refs.current["role"] = el)}
        />
        <Filter
          title="Last name"
          isList={false}
          inputRef={(el) => (refs.current["last_name"] = el)}
        />
        <Filter
          title="Name"
          isList={false}
          inputRef={(el) => (refs.current["first_name"] = el)}
        />
        <Filter
          title="Phone"
          isList={false}
          inputRef={(el) => (refs.current["phone"] = el)}
        />
        <Filter
          title="City"
          isList={false}
          inputRef={(el) => (refs.current["city"] = el)}
        />
        <Filter
          title="Address"
          isList={false}
          inputRef={(el) => (refs.current["adress"] = el)}
        />
        <Filter
          title="Email"
          isList={false}
          inputRef={(el) => (refs.current["email"] = el)}
        />
        <Filter
          title="Telegram"
          isList={false}
          inputRef={(el) => (refs.current["telegram"] = el)}
        />
      </ul>
      <button className={styles.submit} onClick={handleApply}>
        SEARCH
      </button>
      <button className={styles.reset} onClick={handleReset}>
        CLEAR
      </button>
    </div>
  );
}
