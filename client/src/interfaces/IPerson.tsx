import dayjs from "dayjs";

interface date {
  date_from: dayjs.Dayjs;
  date_to: dayjs.Dayjs;
}

export interface IPreson {
  post: string;
  department_path: string;
  department_name: string;
  first_name: string;
  last_name: string;
  birthdate: dayjs.Dayjs | null;
  sex: string | null;
  phone_number: string;
  city: string;
  address: string;
  tg_username: string | null;
  email: string;
  on_sick_leave_info: date | null;
  on_leave_info: date | null;
  boss_id: number;
  about: string;
  role: string;
}
