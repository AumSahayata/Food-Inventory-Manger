"use client";
import Image from "next/image";
import image from "@/public/food.jpg";

import { purchase } from "../actions/purchaseaction";
import toast from "react-hot-toast";

export function ProductCard({ product }: { product: any }) {
  const onPurchase = async (id) => {
    console.log("purchase");
    toast.success(`1 purchased`);
    await purchase(id);
  };
  const discountedPrice = product.discount_percentage
    ? product.price * (1 - product.discount_percentage / 100)
    : product.price;

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <Image
        src={image}
        alt={product.product_name}
        width={200}
        height={200}
        className="w-full h-48 object-cover"
      />
      <div className="p-4">
        <h2 className="text-xl font-semibold mb-2">{product.product_name}</h2>
        <div className="mb-4">
          {product.discount_percentage !== 0 ? (
            <>
              <span className="text-gray-600 line-through mr-2">
                ${product.price.toFixed(2)}
              </span>
              <span className="text-red-600 font-semibold">
                &#8377;{discountedPrice.toFixed(2)}
              </span>
              <span className="ml-2 text-green-600">
                ({product.discount_percentage}% off)
              </span>
            </>
          ) : (
            <span className="text-gray-600">${product.price.toFixed(2)}</span>
          )}
        </div>
        <button
          className="w-full bg-black text-white rounded-md p-4 transition duration-300 ease-in-out
           hover:bg-gray-800 focus:ring-2 focus:ring-offset-2 focus:ring-gray-600 active:scale-95"
          onClick={() => onPurchase(product.p_id)}
        >
          Buy Now
        </button>
      </div>
    </div>
  );
}
