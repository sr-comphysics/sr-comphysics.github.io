%*****************************************************************************************
% Title: GNU Octave: Eigenvector of a Delocalized State with a Quantum Potential
%
% Description:
% This program sets up a discretized one-dimensional domain and builds a tridiagonal
% matrix representation of an operator that includes both the kinetic and potential terms.
% It then computes the eigenvector corresponding to the smallest (algebraic) eigenvalue
% using the "eigs" function. Finally, it plots the eigenvector against the spatial grid.
%
% Compiler/Interpreter Instructions:
% This script is intended to be run in Octave. To execute:
%   1. Save the script as 'delocalized_state.m'.
%   2. In the GNU Octave command window, navigate to the script directory.
%   3. Run the script by typing:
%   >> delocalized_state
%******************************************************************************************

% Define a double well potential function: V(x) = 0.1*(x^2 - 4).^2
potential = @(x) 0.1 * (x.^2 - 4).^2;

% Set graphics toolkit (here, using "gnuplot" for plotting)
graphics_toolkit("gnuplot");

% Define grid parameters:
N = 100;           % Number of discretization points
width = 20;        % Total width of the spatial domain
dx = width / (N - 1);  % Spatial step size calculated from total width and number of points
a = -width / 2;    % Left-most coordinate (centered domain)

% Initialize the matrix (N x N) with zeros
mat = zeros(N, N);

% Create spatial grid array using linspace, from a (left endpoint) to -a (right endpoint)
xR = linspace(a, -a, N);

% Construct the tridiagonal matrix representation:
% The diagonal contains the kinetic diagonal + potential contribution,
% and the off-diagonals represent the finite difference kinetic coupling.
for i = 1:N
    % Diagonal element includes central finite difference term for kinetic energy
    % (corresponding to 1/dx^2) and the potential function evaluated at the grid point.
    mat(i, i) = 1 / dx^2 + potential(xR(i));

    % Off-diagonal element to the right (upper diagonal) represents
    % half the central finite difference term for the kinetic energy.
    if i ~= N
        mat(i, i + 1) = -1 / (2 * dx^2);
    end

    % Off-diagonal element to the left (lower diagonal) similarly represents
    % the half finite difference term for kinetic energy.
    if i ~= 1
        mat(i, i - 1) = -1 / (2 * dx^2);
    end
end

% Compute the eigenvector corresponding to the smallest algebraic eigenvalue
% we use eigs with 'sa' specifying "smallest algebraic" eigenvalue.
[eigne_vectors, eigen_values] = eigs(mat, 1, 'sa');

% Normalize the eigenvector based on the sign of its central component
% to remove the arbitrary global phase in eigenfunctions.
m = round(N / 2);
ad = eigne_vectors * sign(eigne_vectors(m));

% Plot the computed eigenvector against the spatial grid.
plot(xR, ad);
xlabel('x');                          % Label for the x-axis: spatial coordinate
ylabel('Eigenvector amplitude');      % Label for the y-axis: eigenvector amplitude
title('Eigenvector of Delocalized State');  % Title of the plot
grid on;                              % Enable grid for better readability
