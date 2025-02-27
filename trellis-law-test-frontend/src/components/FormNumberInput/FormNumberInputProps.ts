export default FormNumberInputProps;

type FormNumberInputProps = {
  label: string;
  placeholder: string;
  id?: string;
  required?: boolean;
  min?: number;
  max?: number;
  step?: number;
};
