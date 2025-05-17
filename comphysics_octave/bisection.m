% Function to approximate the root of a given function f using the Bisection method.
% Inputs:
%   a - Left endpoint of the initial interval.
%   b - Right endpoint of the initial interval.
%   tol - Tolerance value for convergence.
%   f - Function handle representing the function whose root is to be found.
% Output:
%   result - Approximated root of the function.

function y = bisection(a, b, tol, f)
  % Check if the initial interval [a, b] contains a root.
  if f(a) * f(b) > 0
    error('Function must have opposite signs at endpoints a and b.');
  endif

  % Begin iterative process.
  while (b - a)/2 > tol
    % Compute the midpoint of the current interval.
    c = (a + b) / 2;

    % Evaluate the function at the midpoint.
    fc = f(c);

    % Check if the midpoint is a root or if the interval is sufficiently small.
    if fc == 0 || (b - a)/2 < tol
      y = c;
      return;
    endif

    % Determine the subinterval that contains the root.
    if f(a) * fc < 0
      % The root lies between a and c.
      b = c;
    else
      % The root lies between c and b.
      a = c;
    endif
  endwhile

  % Return the midpoint as the final approximation of the root.
  y = (a + b) / 2;
end

% Compiler/ Interpreter Instruction

% 1. Save the code in a file named, for example, "bisection.m".
% 2. Run GNU Octave (or Octave CLI/GUI).
% 3. In Octave’s command prompt, call the function with the appropriate parameters,
% for example:
% octave:1> f = @(x) x^3 - x - 2;
% octave:2> root = bisection(f, 1.5, 1e-6);
% octave:3> disp(root);
