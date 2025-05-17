% Function to approximate the root of a given function f using the Newton-Raphson method.
% Inputs:
%   f - Function handle representing the function whose root is to be found.
%   a - Initial guess for the root.
%   b - Tolerance value for convergence.
% Output:
%   result - Approximated root of the function.

function result = newton_raphson(a, b, f)
  % Initialize a small step size (dx) for numerical derivative calculation.
  dx = 1.e-3;

  % Perform a maximum of 5 Newton-Raphson iterations.
  for loop = 1:5
    % Approximate the derivative of f at point a using symmetric difference.
    d = (f(a + dx) - f(a - dx)) / (2 * dx);

    % Calculate the Newton-Raphson update step: dx = -f(a) / f'(a).
    dx = -f(a) / d;

    % Update the current guess for the root.
    a += dx;

    % Check for convergence: if the step size is less than the tolerance, stop iterating.
    if abs(dx) < b
      break;
    end
  endfor

  % Return the final approximation of the root.
  result = a;
end

% Compiler/ Interpreter Instruction

% 1. Save the code in a file named, for example, "newton_raphson.m".
% 2. Run GNU Octave (or Octave CLI/GUI).
% 3. In Octave’s command prompt, call the function with the appropriate parameters,
% for example:
% octave:1> f = @(x) x^3 - x - 2;
% octave:2> root = newton(f, 1.5, 1e-6);
% octave:3> disp(root);
