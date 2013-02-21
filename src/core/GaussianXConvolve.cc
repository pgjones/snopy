#include <TH2D.h>
#include <TFile.h>
#include <TH1D.h>

TH2D* 
GaussianXConvolve( TH2D* result_spectrum, TH2D* raw_spectrum, TH2D* sigma )
{
  for( int binR = 1; binR <= raw_spectrum->GetNbinsY(); binR++ )
    {
      for( int b1 = 1; b1 <= raw_spectrum->GetNbinsX(); b1++ )
        {
          double h = 0.0;
          for( int b2 = 1; b2 <= raw_spectrum->GetNbinsX(); b2++ )
            {
              if( raw_spectrum->GetBinContent( b2, binR ) <= 0.0 )
                continue;
              const double sigma_ = sigma->GetBinContent( b2, binR );
              const double c = sigma_ / raw_spectrum->GetXaxis()->GetBinWidth( b1 );
              const double N = 1.0 / ( c * sqrt( 2.0 * 3.14 ) );
              h += raw_spectrum->GetBinContent( b2, binR ) * N * exp( -pow( b1 - b2, 2.0 ) / ( 2.0 * pow( c, 2.0 ) ) );
            }
          result_spectrum->SetBinContent( b1, binR, h );
        }
    }
  return result_spectrum;
}

TH1D*
ConvolveReject( TH1D* convolved, TH1D* spectra1, TH1D* spectra2 )
{
  // (c)(b1) = sum(b2) h1(b2) * h2( b1 - b2 )                                                                                                   
  for( int b1 = 1; b1 <= convolved->GetNbinsX(); b1++ )
    {
      double h = 0.0;
      for( int b2 = 1; b2 <= convolved->GetNbinsX(); b2++ )
        {
          int diff = b1 - b2;
          if( diff >= 1 && diff <= convolved->GetNbinsX() )
            {
              h = h + spectra1->GetBinContent( b2 ) * spectra2->GetBinContent( diff );
              convolved->SetBinContent( b1, h );
            }
        }
    }
  return convolved;
}
