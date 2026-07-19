{
  description = "Reproducible development environment for the Astro portfolio website and Typst CV";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Web Page Dev Stack
            nodejs_22
            nodePackages.npm

            # CV Compilation Stack
            typst
          ];

          shellHook = ''
            echo "================================================================="
            echo "🚀 reproducible Portfolio & CV Environment Active via Nix Flakes"
            echo "   Node.js : $(node --version)"
            echo "   NPM     : $(npm --version)"
            echo "   Typst   : $(typst --version | head -n1)"
            echo "================================================================="
          '';
        };
      }
    );
}
