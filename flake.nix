{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
  };
  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    LOCALE_ARCHIVE = "${pkgs.glibcLocales}/lib/locale/locale-archive";
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [
        python311Packages.pudb
        python311Packages.pygame
      ];
    };
  };
}
