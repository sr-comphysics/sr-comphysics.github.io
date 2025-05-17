% Function to approximate the integral of a given function f using the trapezoidal rule.
% Inputs:
%   a - Left endpoint of the interval.
%   b - Right endpoint of the interval.
%   n - Number of subintervals in which the interval [a,b] is divided.
%   f - Function handle representing the function to integrate.
% Output:
%   y - Approximated value of the definite integral.

function y = trapezoidal(a, b, n, f)
  % Compute the width (h) of each subinterval.
  h = (b-a)/n;

  % Initialize the sum (s) with the average of the function values at the endpoints.
  s = ((f(a) + f(b))/2);

  % Loop over the interior points of the interval.
  for i = 1:(n-1)
    % Add the function value at each interior point to the sum.
    % a + i*h computes the current x-value.
    s += f(a + i*h);
  endfor

  % Multiply the sum by the subinterval width to obtain the integral approximation.
  y = h*s;
end

% Compiler/ Interpreter Instruction

% 1. Save the code in a file named, for example, "trapezoidal.m".
% 2. Run GNU Octave (or Octave CLI/GUI).
% 3. In Octave’s command prompt, call the function with the appropriate parameters,
% for example:
% octave:1> result = trapezoidal(0, 1, 100, @(x) x.^2);
