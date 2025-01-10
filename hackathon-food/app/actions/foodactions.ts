"use server";

import { currentUser } from "@clerk/nextjs/server";
import { revalidatePath } from "next/cache";

export const addProduct = async (productName, category, price) => {
  const current = await currentUser();
  await fetch(`${process.env.BASE_URL}/api/inv/add/product`, {
    method: "POST",
    body: JSON.stringify({
      name: productName,
      category: category,
      price: price,
      vendor_id: current?.id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  revalidatePath("/products");
};

export const addInventory = async (productId, quantity, date) => {
  const current = await currentUser();
  await fetch(`${process.env.BASE_URL}/api/inv/add`, {
    method: "POST",
    body: JSON.stringify({
      quantity: Number(quantity),
      product_id: productId,
      expiry_date: date,
      vendor_id: current?.id,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
  revalidatePath("/");
};

export const discount = async (batchId, percent) => {
  await fetch(`${process.env.BASE_URL}/api/inv/discount`, {
    method: "PATCH",
    body: JSON.stringify({
      batch_id: batchId,
      is_discounted: true,
      discount_percentage: Number(percent),
    }),
    headers: {
      "Content-Type": "application/json",
    },
  });
};
