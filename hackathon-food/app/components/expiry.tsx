"use client";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogFooter,
} from "@/components/ui/dialog";
import {
  Table,
  TableBody,
  TableHead,
  TableCell,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

import { useState } from "react";

import { discount } from "../actions/foodactions";

const Expiry = ({ data }) => {
  const [batchId, setBatchId] = useState("");
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [discountPercent, setDiscountPercent] = useState("");

  return (
    <div>
      <div className="flex flex-col gap-4 mx-9">
        <main className="flex justify-between items-center max-w-full py-6">
          <h1 className="text-3xl font-bold tracking-wide">
            Products Nearing Expiry
          </h1>
        </main>
        <Table className="w-full">
          <TableHeader>
            <TableRow>
              <TableHead>Batch Id</TableHead>
              <TableHead>Product Name</TableHead>
              <TableHead>Days Remaining (Till Expiry)</TableHead>
              <TableHead colSpan={1}></TableHead>
            </TableRow>
          </TableHeader>

          <TableBody>
            {data.map((inven) => {
              return (
                <TableRow key={inven.batch_id}>
                  <TableCell>{inven.batch_id}</TableCell>
                  <TableCell>{inven.product_name}</TableCell>
                  <TableCell>{inven.days_remaining}</TableCell>
                  <TableCell>
                    <Button
                      onClick={() => {
                        setBatchId(inven.batch_id);
                        setIsDialogOpen(true);
                      }}
                    >
                      Apply Discount
                    </Button>
                  </TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </div>
      <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Apply Discount</DialogTitle>
          </DialogHeader>
          <div className="py-4">
            <Label htmlFor="discountPercent">Discount Percentage</Label>
            <Input
              id="discountPercent"
              type="number"
              min="0"
              max="100"
              value={discountPercent}
              onChange={(e) => setDiscountPercent(e.target.value)}
              placeholder="Enter discount percentage"
            />
          </div>
          <DialogFooter>
            <Button
              onClick={() => {
                setIsDialogOpen(false);
                discount(batchId, discountPercent);
              }}
            >
              Apply
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  );
};
export default Expiry;
