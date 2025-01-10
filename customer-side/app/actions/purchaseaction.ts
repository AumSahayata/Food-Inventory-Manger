"use server";
export const purchase = async (id) => {
  await fetch(`http://127.0.0.1:8000/api/inv/buy/${id}`, {
    method: "PATCH",
  });
};
