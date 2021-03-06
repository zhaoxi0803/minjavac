class Factorial:

procedure Factorial@main
   ; Block     : 0
   ; adj       : []
   ; write     : [.call, .void, .new_Fac]
   ; read      : [.call, .new_Fac]
   ; firstRead : []
   ; live      : []
   save_context;
   .new_Fac := call Fac@@new;
   load_context;
   save_context;
   param 5;
   param .new_Fac;
   .call := call Fac@ComputeFac;
   load_context;
   save_c_context;
   param .call;
   .void := call _print_int;
   load_c_context;
end
end

class Fac:

procedure Fac@ComputeFac
   ; Block     : 0
   ; adj       : [2, 1]
   ; write     : [.add_A, .new_array, .add, .facNum, y, x]
   ; read      : [.add_A, num, .new_array, .add, y, .facNum, x]
   ; firstRead : [num]
   ; live      : []
   save_c_context;
   param 3;
   .new_array := call _new_array;
   load_c_context;
   x := .new_array;
   .add := add 0, 1;
   x[.add] := 3;
   y := x;
   .add_A := add 0, 2;
   .facNum := facNum;
   y[.add_A] := .facNum;
   if greater_or_equal(num, 1) goto .if_false;

   ; Block     : 1
   ; adj       : [3]
   ; write     : [num_aux]
   ; read      : []
   ; firstRead : []
   ; live      : [num_aux]
   num_aux := 1;
   goto .if_next;

   ; Block     : 2
   ; adj       : [3]
   ; write     : [.call, .mult, .sub, num_aux]
   ; read      : [.call, .mult, num, .sub]
   ; firstRead : [num]
   ; live      : [num_aux]
 .if_false:
   save_context;
   .sub := sub num, 1;
   param .sub;
   param this;
   .call := call Fac@ComputeFac;
   load_context;
   .mult := mult num, .call;
   num_aux := .mult;

   ; Block     : 3
   ; adj       : []
   ; write     : []
   ; read      : [num_aux]
   ; firstRead : [num_aux]
   ; live      : []
 .if_next:
   return num_aux;
end
end