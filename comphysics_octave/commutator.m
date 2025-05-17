% Title: Computation of the Commutator of Two Matrices
%
% Function to compute the commutator of two square matrices A and B.
% The commutator is defined as [A, B] = AB - BA.
%
% Inputs:
%   A - A square matrix.
%   B - Another square matrix of the same size as A.
%
% Output:
%   C - The commutator matrix, computed as C = AB - BA.

function C = commutator(A, B)
  % Compute the product of A and B
  AB = A * B;

  % Compute the product of B and A
  BA = B * A;

  % Subtract BA from AB to get the commutator
  C = AB - BA;
end

% 1. Save the code in a file named "commutator.m".
% 2. Open GNU Octave.
% 3. In the Octave command prompt, call the function with square matrices A and B:
% octave:1> A = [0 1; -1 0];
% octave:2> B = [1 0; 0 -1];
% octave:3> C = commutator(A, B);
% octave:4> disp(C);
% 4. The output will be the matrix commutator [A, B] = AB - BA.
