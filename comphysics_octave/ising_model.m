%**************************************************************************
% Title: Ising Model Statistical Analysis and Specific Heat Calculation
%
% Description:
% This GNU Octave script computes the statistical properties of the Ising model
% on a one-dimensional spin chain with periodic boundary conditions.
% It calculates the partition function, average energy per configuration,
% and the specific heat per spin at a given inverse temperature beta.
%
% Compiler/Interpreter Instructions:
% This script is intended to be run in MATLAB or Octave. To execute:
%   1. Save the script as 'ising_model.m'.
%   2. In the GNU Octave command window, navigate to the script directory.
%   3. Run the script by typing:
%   >> ising_model
%
%**************************************************************************

% Initialize the Ising model structure with short variable names

I.nE = 1;       % numberOfEnergies (initial count of distinct energy levels)
I.E(1) = 0;     % energy values, here starting with one energy value of 0
I.g(1) = 0;     % numberOfStates (degeneracy): count for configurations having a given energy

N = 10;          % numberOfSpins: total spins in the one-dimensional chain
NR = 2^N;       % numberOfRealizations: total configurations (2^numberOfSpins)

for l = 1:NR
  % Convert each number (0 to 2^N - 1) into binary form representing spins.
  % Each configuration is represented as a binary string of length N.
  s = dec2bin(l - 1, N);
  E = 0;  % Initialize temporary energy for the current spin configuration

  % Compute the Ising energy for the configuration (interaction constant = -1)
  for j = 1:N
    % Determine neighbor index with periodic boundary conditions
    % (wraps around such that the neighbor of the last spin is the first spin)
    j_n = mod(j, N) + 1;

    % Convert the character '0' or '1' to a numeric value for spin at position j
    s1 = str2num(s(j));    %#ok<ST2NM>
    % Convert the neighbor spin (at position j_n) from character to numeric
    s2 = str2num(s(j_n));  %#ok<ST2NM>

    % Update energy: interaction energy is -s1 * s2 for the pair (j, j_n)
    E = E + s1 * s2;
  end

  % Check if the computed energy E is already in the list of energies
  found = 0;
  for k = 1:I.nE
    if I.E(k) == E
      % If the energy is already present, increment its degeneracy count
      I.g(k) = I.g(k) + 1;
      found = 1;  % Mark that the energy level has been found
      break;
    end
  end

  % If the energy E has not been encountered before, add as a new level
  if found == 0
    I.nE = I.nE + 1;
    I.E(I.nE) = E;
    I.g(I.nE) = 1;
  end
end

% Calculate statistical quantities for a given inverse temperature, beta.
b = 0.1;       % myBeta: inverse temperature, beta = 1/(kT)
Z = 0;          % partitionFunction: will sum over all energies weighted by degeneracy

% Compute the partition function Z = Σ[g(E)*exp(-beta*E)]
for k = 1:I.nE
  Z = Z + I.g(k) * exp(-b * I.E(k));
end

E_avg = 0;    % Average Energy initialization
E2_avg = 0;   % Average of Energy squared initialization

% Compute the weighted averages for energy and energy squared
for k = 1:I.nE
  E_avg = E_avg + I.E(k) * I.g(k) * exp(-b * I.E(k));
  E2_avg = E2_avg + (I.E(k)^2) * I.g(k) * exp(-b * I.E(k));
end

% Normalize the averages by the partition function to get expectation values
E_avg = E_avg / Z;
E2_avg = E2_avg / Z;

% Calculate the specific heat per spin: C = beta^2 * (⟨E^2⟩ - ⟨E⟩^2) / N
C = b^2 * (E2_avg - E_avg^2) / N;

% Display the computed statistical results
fprintf('Z (Partition Function): %f\n', Z);
fprintf('E_avg (Average Energy): %f\n', E_avg);
fprintf('C (Specific Heat per Spin): %f\n', C);
