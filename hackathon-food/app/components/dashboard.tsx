"use client";
import {
  Dialog,
  DialogTrigger,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import {
  Table,
  TableBody,
  TableHead,
  TableCell,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";

import { AddInventoryForm } from "../components/add-inventory-form";

import { useState } from "react";

const Dashboard = ({ data, inven }) => {
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  return (
    <div>
      <div className="flex flex-col gap-4 mx-9">
        <main className="flex justify-between items-center max-w-full py-6">
          <h1 className="text-3xl font-bold tracking-wide">Inventory</h1>
          <div className="px-4 py-6 sm:px-0">
            <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
              <DialogTrigger asChild>
                <Button>Add Inventory</Button>
              </DialogTrigger>
              <DialogContent>
                <DialogHeader>
                  <DialogTitle>Add New Inventory</DialogTitle>
                </DialogHeader>
                <AddInventoryForm
                  data={data}
                  onClose={() => setIsDialogOpen(false)}
                />
              </DialogContent>
            </Dialog>
          </div>
        </main>
        <Table className="w-full">
          <TableHeader>
            <TableRow>
              <TableHead>Batch Id</TableHead>
              <TableHead>Product</TableHead>
              <TableHead>Quantity</TableHead>
              <TableHead>Expiry Date</TableHead>
              <TableHead colSpan={1}></TableHead>
            </TableRow>
          </TableHeader>

          <TableBody>
            {inven.map((inven) => {
              return (
                <TableRow key={inven.batch_id}>
                  <TableCell>{inven.batch_id}</TableCell>
                  <TableCell>{inven.product_name}</TableCell>
                  <TableCell>{inven.quantity}</TableCell>
                  <TableCell>{inven.expiry_date}</TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </div>
    </div>
  );
};

export default Dashboard;
