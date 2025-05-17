% Title: Solving the Time-Independent Schrödinger Equation for a Particle in a 1D Box
%
% Function to compute and plot the eigenfunctions of a quantum particle confined in a 1D box.
% This method uses the finite difference approach to construct the Hamiltonian matrix and solve
% the time-independent Schrödinger equation.
%
% No input/output arguments – the function builds the domain, solves the eigenvalue problem,
% and plots the resulting eigenfunctions.

function particle_in_box()
  % Set up graphics environment.
  graphics_toolkit("gnuplot");

  % Physical constants (set to 1 for simplicity)
  hbar = 1;         % Reduced Planck’s constant
  m = 1;            % Mass of the particle

  % Spatial domain parameters
  L = 2 * pi;       % Length of the 1D box
  N = 100;          % Number of spatial grid points
  dx = L / (N - 1); % Grid spacing
  x = 0:dx:L;       % Spatial grid from 0 to L

  % Construct the second derivative matrix (Laplacian) using central differences
  laplacian = (-2 * diag(ones(N, 1), 0) + ...
                diag(ones(N - 1, 1), 1) + ...
                diag(ones(N - 1, 1), -1)) / dx^2;

  % Apply Dirichlet boundary conditions (wavefunction is zero at boundaries)
  laplacian(1, :) = 0;
  laplacian(N, :) = 0;

  % Construct the Hamiltonian operator H = -(ħ² / 2m) * d²/dx²
  H = -(hbar^2 / (2 * m)) * laplacian;

  % Solve the eigenvalue problem H * psi = E * psi
  [psi, E] = eig(H);

  % Plot the first few eigenfunctions (wavefunctions) for different quantum numbers
  plot(x, psi(:,1), "k-", ...    % First eigenfunction (n=1)
       x, psi(:,2), "r-", ...    % Second eigenfunction (n=2)
       x, psi(:,3), "b-", ...    % Third eigenfunction (n=3)
       x, psi(:,6), "k-.");      % Sixth eigenfunction (n=6)

  % Annotate the plot
  legend("n=1", "n=2", "n=3", "n=6");
  axis([0 L -0.2 0.2]);
  title("Eigenfunctions for a Particle in a Box");
  xlabel("x");
  ylabel("\psi(x)");
end

% Compiler/ Interpreter Instruction
% 1. Save the code in a file named, for example, "particle_in_box.m".
% 2. Open GNU Octave (GUI or CLI).
% 3. In the Octave command prompt, call the function:
% octave:1> particle_in_box
% 4. A plot window will appear showing the eigenfunctions of the particle in a 1D box.
