export default interface MessageCardProps {
  compact?: boolean;
  type: 'success' | 'error';
  title: string;
  message: string | null;
}
