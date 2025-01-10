const mockSalesData = [
  { date: "2025-01-01", sales_quantity: 10 },
  { date: "2025-01-02", sales_quantity: 15 },
  { date: "2025-01-03", sales_quantity: 8 },
  { date: "2025-01-04", sales_quantity: 12 },
];

import SalesOverTime from "../components/sales-over-time";
export default function SalesPage() {
  return <SalesOverTime salesData={mockSalesData} />;
}
