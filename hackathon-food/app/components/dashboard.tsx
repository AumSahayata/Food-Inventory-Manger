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
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Button } from "@/components/ui/button";


import { AddInventoryForm } from "../components/add-inventory-form";

import { useState } from "react";

const Dashboard = () => {
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
                <AddInventoryForm onClose={() => setIsDialogOpen(false)} />
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
              <TableHead>Expiry In (Days)</TableHead>
              <TableHead colSpan={1}></TableHead>
            </TableRow>
          </TableHeader>

          <TableBody></TableBody>
        </Table>
      </div>
    </div>
  );
};

export default Dashboard;
