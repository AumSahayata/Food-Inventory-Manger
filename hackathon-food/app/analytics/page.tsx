const mockSalesData = [
  { date: "2025-01-01", sales_quantity: 10 },
  { date: "2025-01-02", sales_quantity: 15 },
  { date: "2025-01-03", sales_quantity: 8 },
  { date: "2025-01-04", sales_quantity: 12 },
];

import { currentUser } from "@clerk/nextjs/server";

const getProduct = async (id) => {
  console.log(id);
  const response = await fetch(`${process.env.BASE_URL}/api/inv/all/${id}`);
  const data = await response.json();
  console.log(data);
  return data;
};
const getSales = async (productId) => {
  //   const response = await fetch(
  //     `${process.env.BASE_URL}/api/inv/products/${id}`
  //   );
  //   const data = await response.json();
  //   return data;
};
import SalesOverTime from "../components/sales-over-time";
export default async function SalesPage() {
  const user = await currentUser();
  const product = await getProduct(user?.id);
  const getSalesData = async (productId) => {
    "use server";
    const salesData = await getSales(productId);
  };

  return (
    <SalesOverTime
      salesData={mockSalesData}
      data={product}
      func={getSalesData}
    />
  );
}
